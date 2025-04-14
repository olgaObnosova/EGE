strok=input()
if len(strok)<=7 and 'нота' not in strok and strok < 'флейта':
    if (('до' in strok or 'ля' in strok) and len(strok)%2==0)\
        or ('соль' in strok and len(strok)%2!=0):
        print('может')
else:
    print('не может')