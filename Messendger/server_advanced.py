import os
import base64
import json
from flask import Flask, render_template, request, jsonify, send_file
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime
import secrets

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB для файлов
socketio = SocketIO(app, cors_allowed_origins="*")

# Хранилище данных
active_users = {}
private_rooms = {}
messages = {}
unread_messages = {}
typing_users = {}
pinned_messages = {}
call_requests = {}
uploaded_files = {}

# Создаем папку для загрузок
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('chat_advanced.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Загрузка файлов (изображения, аудио, документы)"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file'}), 400
        
        file = request.files['file']
        username = request.form.get('username')
        room = request.form.get('room', 'general')
        
        if file.filename == '':
            return jsonify({'error': 'Empty filename'}), 400
        
        # Сохраняем файл
        file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else 'bin'
        file_name = f"{datetime.now().timestamp()}_{secrets.token_hex(8)}.{file_ext}"
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        file.save(file_path)
        
        file_size = os.path.getsize(file_path)
        file_type = 'image' if file_ext in ['jpg', 'jpeg', 'png', 'gif', 'webp'] else 'audio' if file_ext in ['mp3', 'wav', 'ogg', 'm4a'] else 'document'
        
        # Сохраняем информацию о файле
        file_info = {
            'filename': file.filename,
            'saved_name': file_name,
            'size': file_size,
            'type': file_type,
            'ext': file_ext
        }
        uploaded_files[file_name] = file_info
        
        # Создаем сообщение
        msg_obj = {
            'username': username,
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': file_type,
            'file_info': file_info,
            'isFile': True
        }
        
        if room not in messages:
            messages[room] = []
        messages[room].append(msg_obj)
        
        if len(messages[room]) > 500:
            messages[room].pop(0)
        
        socketio.emit('new_message', msg_obj, room=room)
        
        return jsonify({'success': True, 'file_info': file_info})
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    """Скачивание файла"""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        original_name = uploaded_files.get(filename, {}).get('filename', filename)
        return send_file(file_path, as_attachment=True, download_name=original_name)
    return jsonify({'error': 'File not found'}), 404

@app.route('/search_messages')
def search_messages():
    """Поиск по сообщениям"""
    query = request.args.get('q', '').lower()
    room = request.args.get('room', 'general')
    
    if not query or room not in messages:
        return jsonify({'results': []})
    
    results = []
    for msg in messages[room]:
        if 'message' in msg and query in msg['message'].lower():
            results.append({
                'username': msg['username'],
                'message': msg['message'],
                'timestamp': msg['timestamp'],
                'type': msg.get('type', 'text')
            })
    
    return jsonify({'results': results[-30:]})  # Последние 30 результатов

@app.route('/get_pinned')
def get_pinned():
    """Получить закрепленные сообщения"""
    room = request.args.get('room', 'general')
    return jsonify({'pinned': pinned_messages.get(room, [])})

@socketio.on('connect')
def handle_connect():
    print(f'✅ Клиент подключился: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in active_users:
        username = active_users[request.sid]['username']
        room = active_users[request.sid]['room']
        room_type = active_users[request.sid].get('room_type', 'public')
        
        if room in typing_users and username in typing_users.get(room, []):
            typing_users[room].remove(username)
            emit('typing_update', {'users': typing_users.get(room, [])}, room=room)
        
        if room_type == 'private' and room in private_rooms:
            for sid, user_data in active_users.items():
                if user_data.get('room') == room and sid != request.sid:
                    emit('partner_left', {'message': f'{username} покинул разговор'}, room=sid)
                    break
            if room in private_rooms:
                del private_rooms[room]
        
        del active_users[request.sid]
        
        if room_type != 'private':
            emit('user_left', {'username': username, 'users': get_users_list('general')}, room='general')
            emit('system_message', {'message': f'👋 {username} покинул чат'}, room='general')

@socketio.on('join')
def handle_join(data):
    username = data.get('username')
    room = data.get('room', 'general')
    
    if not username:
        return
    
    for sid, user_data in active_users.items():
        if user_data['username'] == username:
            emit('error', {'message': '❌ Имя уже занято'})
            return
    
    if room not in messages:
        messages[room] = []
    if room not in typing_users:
        typing_users[room] = []
    if username not in unread_messages:
        unread_messages[username] = {}
    if room not in pinned_messages:
        pinned_messages[room] = []
    
    active_users[request.sid] = {'username': username, 'room': room, 'room_type': 'public'}
    join_room(room)
    
    emit('joined', {
        'username': username,
        'room': room,
        'messages': messages[room][-100:],
        'unread': unread_messages.get(username, {}),
        'pinned': pinned_messages.get(room, [])
    })
    
    emit('user_joined', {'username': username, 'users': get_users_list(room)}, room=room)
    emit('system_message', {'message': f'✨ {username} присоединился к чату'}, room=room)

@socketio.on('typing_start')
def handle_typing_start(data):
    username = data.get('username')
    room = data.get('room', 'general')
    
    if room not in typing_users:
        typing_users[room] = []
    
    if username not in typing_users[room]:
        typing_users[room].append(username)
        emit('typing_update', {'users': typing_users[room]}, room=room)

@socketio.on('typing_stop')
def handle_typing_stop(data):
    username = data.get('username')
    room = data.get('room', 'general')
    
    if room in typing_users and username in typing_users[room]:
        typing_users[room].remove(username)
        emit('typing_update', {'users': typing_users[room]}, room=room)

@socketio.on('send_message')
def handle_send_message(data):
    if request.sid not in active_users:
        return
    
    username = active_users[request.sid]['username']
    message = data.get('message', '').strip()
    target_user = data.get('target')
    reply_to = data.get('reply_to')
    
    if not message:
        return
    
    msg_obj = {
        'username': username,
        'message': message,
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'type': 'text',
        'id': secrets.token_hex(8)
    }
    
    if reply_to:
        msg_obj['reply_to'] = reply_to
    
    if target_user:
        target_sid = None
        for sid, user_data in active_users.items():
            if user_data['username'] == target_user:
                target_sid = sid
                break
        
        if target_sid:
            emit('private_message', msg_obj, room=target_sid)
            if target_user not in unread_messages:
                unread_messages[target_user] = {}
            unread_messages[target_user][username] = unread_messages[target_user].get(username, 0) + 1
            emit('unread_update', {'from': username, 'count': unread_messages[target_user][username]}, room=target_sid)
            msg_obj['target'] = target_user
            emit('private_message_sent', msg_obj, room=request.sid)
    else:
        room = active_users[request.sid]['room']
        messages[room].append(msg_obj)
        
        if len(messages[room]) > 500:
            messages[room].pop(0)
        
        emit('new_message', msg_obj, room=room)
        
        for sid, user_data in active_users.items():
            if user_data.get('room') == room and user_data['username'] != username:
                if user_data['username'] not in unread_messages:
                    unread_messages[user_data['username']] = {}
                unread_messages[user_data['username']][username] = unread_messages[user_data['username']].get(username, 0) + 1
                emit('unread_update', {'from': username, 'count': unread_messages[user_data['username']][username]}, room=sid)

@socketio.on('pin_message')
def handle_pin_message(data):
    username = data.get('username')
    message = data.get('message')
    room = data.get('room', 'general')
    
    if room not in pinned_messages:
        pinned_messages[room] = []
    
    pinned_messages[room].append({
        **message,
        'pinned_by': username,
        'pinned_at': datetime.now().strftime('%H:%M:%S')
    })
    
    emit('message_pinned', {'message': message, 'pinned_by': username}, room=room)

@socketio.on('unpin_message')
def handle_unpin_message(data):
    message_id = data.get('message_id')
    room = data.get('room', 'general')
    
    if room in pinned_messages:
        pinned_messages[room] = [m for m in pinned_messages[room] if m.get('id') != message_id]
        emit('message_unpinned', {'message_id': message_id}, room=room)

@socketio.on('mark_read')
def handle_mark_read(data):
    username = data.get('username')
    from_user = data.get('from_user')
    
    if username in unread_messages and from_user in unread_messages[username]:
        del unread_messages[username][from_user]

@socketio.on('invite_user')
def handle_invite(data):
    inviter = data.get('inviter')
    target = data.get('target')
    
    target_sid = None
    for sid, user_data in active_users.items():
        if user_data['username'] == target:
            target_sid = sid
            break
    
    if not target_sid:
        emit('error', {'message': f'❌ Пользователь {target} не найден'}, room=request.sid)
        return
    
    room_name = f"private_{inviter}_{target}_{int(datetime.now().timestamp())}"
    
    emit('call_incoming', {'from': inviter, 'room': room_name}, room=target_sid)
    emit('system_message', {'message': f'📞 Приглашение отправлено {target}'}, room=request.sid)

@socketio.on('accept_call')
def handle_accept_call(data):
    target = data.get('target')
    inviter = data.get('inviter')
    room_name = data.get('room')
    
    inviter_sid = None
    target_sid = None
    
    for sid, user_data in active_users.items():
        if user_data['username'] == inviter:
            inviter_sid = sid
        if user_data['username'] == target:
            target_sid = sid
    
    if not inviter_sid or not target_sid:
        return
    
    active_users[inviter_sid]['room'] = room_name
    active_users[inviter_sid]['room_type'] = 'private'
    active_users[target_sid]['room'] = room_name
    active_users[target_sid]['room_type'] = 'private'
    
    join_room(room_name, sid=inviter_sid)
    join_room(room_name, sid=target_sid)
    
    private_rooms[room_name] = {'user1': inviter, 'user2': target}
    
    if room_name not in messages:
        messages[room_name] = []
    
    emit('call_accepted', {'partner': target, 'room': room_name}, room=inviter_sid)
    emit('call_accepted', {'partner': inviter, 'room': room_name}, room=target_sid)

@socketio.on('decline_call')
def handle_decline_call(data):
    target = data.get('target')
    inviter = data.get('inviter')
    
    inviter_sid = None
    for sid, user_data in active_users.items():
        if user_data['username'] == inviter:
            inviter_sid = sid
            break
    
    if inviter_sid:
        emit('call_declined', {'message': f'❌ {target} отклонил(а) приглашение'}, room=inviter_sid)

@socketio.on('leave_private_chat')
def handle_leave_private(data):
    username = data.get('username')
    room_name = data.get('room')
    
    user_sid = None
    for sid, user_data in active_users.items():
        if user_data['username'] == username:
            user_sid = sid
            break
    
    if not user_sid:
        return
    
    active_users[user_sid]['room'] = 'general'
    active_users[user_sid]['room_type'] = 'public'
    
    leave_room(room_name, sid=user_sid)
    join_room('general', sid=user_sid)
    
    for sid, user_data in active_users.items():
        if user_data.get('room') == room_name and user_data['username'] != username:
            emit('partner_left', {'message': f'👋 {username} покинул приватный чат'}, room=sid)
            active_users[sid]['room'] = 'general'
            active_users[sid]['room_type'] = 'public'
            leave_room(room_name, sid=sid)
            join_room('general', sid=sid)
            break
    
    emit('left_private', {'message': 'Вы вернулись в общий чат'}, room=user_sid)

def get_users_list(room):
    users = []
    for user_data in active_users.values():
        if user_data.get('room') == room:
            users.append(user_data['username'])
    return users

if __name__ == '__main__':
    print("=" * 60)
    print("🎙️  МЕССЕНДЖЕР С РАСШИРЕННЫМИ ФУНКЦИЯМИ")
    print("=" * 60)
    print("✨ Функции:")
    print("   • 🎤 Голосовые сообщения (запись и отправка)")
    print("   • 📎 Отправка любых файлов")
    print("   • 🔍 Поиск по сообщениям")
    print("   • 📌 Закрепленные сообщения")
    print("   • 🌙 Темная тема")
    print("   • Статус 'печатает...'")
    print("   • Непрочитанные сообщения")
    print("=" * 60)
    print("🌐 Откройте в браузере: http://localhost:5000")
    print("=" * 60)
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)