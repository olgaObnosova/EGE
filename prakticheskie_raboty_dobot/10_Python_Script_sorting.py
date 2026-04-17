#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Практическая работа №3: Автоматизация сортировки
Программа для управления роботом Dobot Magician на Python
"""

import time
try:
    from pydobot import Dobot
except ImportError:
    print("Ошибка: библиотека pydobot не установлена.")
    print("Установите её командой: pip install pydobot")
    exit(1)

class DobotSorter:
    """Класс для управления сортировкой объектов с помощью Dobot Magician"""
    
    def __init__(self, port='COM3'):
        """
        Инициализация подключения к роботу
        
        Args:
            port (str): COM-порт для подключения (например, 'COM3', '/dev/ttyUSB0')
        """
        self.port = port
        self.robot = None
        self.is_connected = False
        
        # Координаты точек (ЗАМЕНИТЕ НА СВОИ ПОСЛЕ КАЛИБРОВКИ!)
        # Точки подхода (над объектами)
        self.pick_approach_z = -70  # Высота подхода к объекту
        self.place_approach_z = -70  # Высота подхода к месту выгрузки
        
        # Точки захвата объектов (координаты кубиков)
        self.pick_positions = [
            (200, 0, -85),   # Кубик 1
            (210, 0, -85),   # Кубик 2
            (220, 0, -85),   # Кубик 3
            (230, 0, -85),   # Кубик 4
            (240, 0, -85),   # Кубик 5
        ]
        
        # Точки выгрузки (для сортировки по цвету)
        self.place_positions = {
            'red': (300, 50, -85),    # Зона для красных кубиков
            'blue': (350, 50, -85),   # Зона для синих кубиков
            'default': (300, 50, -85) # Зона по умолчанию
        }
        
        # Скорость перемещения
        self.velocity = 60
        
    def connect(self):
        """Подключение к роботу"""
        try:
            print(f"Подключение к роботу на порту {self.port}...")
            self.robot = Dobot(port=self.port)
            self.is_connected = True
            print("✓ Подключение успешно!")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"✗ Ошибка подключения: {e}")
            return False
    
    def disconnect(self):
        """Отключение от робота"""
        if self.robot and self.is_connected:
            self.robot.close()
            self.is_connected = False
            print("✓ Соединение закрыто")
    
    def move_to(self, x, y, z, wait=True):
        """Перемещение в указанную точку"""
        if not self.is_connected:
            print("Ошибка: робот не подключен")
            return False
        try:
            self.robot.move_to(x, y, z, wait=wait)
            return True
        except Exception as e:
            print(f"Ошибка при перемещении: {e}")
            return False
    
    def suction_on(self):
        """Включение присоски (захват)"""
        if self.is_connected:
            self.robot.suck(True)
            time.sleep(1)
    
    def suction_off(self):
        """Выключение присоски (отпускание)"""
        if self.is_connected:
            self.robot.suck(False)
            time.sleep(1)
    
    def move_single_cube(self, pick_pos, place_pos):
        """
        Перемещение одного кубика из точки pick_pos в точку place_pos
        
        Args:
            pick_pos (tuple): координаты захвата (x, y, z)
            place_pos (tuple): координаты выгрузки (x, y, z)
        """
        pick_x, pick_y, pick_z = pick_pos
        place_x, place_y, place_z = place_pos
        
        print(f"  Перемещение из ({pick_x}, {pick_y}) в ({place_x}, {place_y})")
        
        # Подход к кубику
        self.move_to(pick_x, pick_y, self.pick_approach_z)
        time.sleep(0.5)
        
        # Опускание к кубику
        self.move_to(pick_x, pick_y, pick_z)
        time.sleep(0.5)
        
        # Захват
        self.suction_on()
        
        # Подъем с кубиком
        self.move_to(pick_x, pick_y, self.pick_approach_z)
        time.sleep(0.5)
        
        # Перемещение к месту выгрузки
        self.move_to(place_x, place_y, self.place_approach_z)
        time.sleep(0.5)
        
        # Опускание для выгрузки
        self.move_to(place_x, place_y, place_z)
        time.sleep(0.5)
        
        # Отпускание
        self.suction_off()
        
        # Подъем после выгрузки
        self.move_to(place_x, place_y, self.place_approach_z)
        time.sleep(0.5)
        
        print(f"  ✓ Кубик перемещен")
    
    def sort_all_cubes(self):
        """Перемещение всех кубиков в зону по умолчанию"""
        print("\n" + "="*50)
        print("НАЧАЛО СОРТИРОВКИ ВСЕХ КУБИКОВ")
        print("="*50)
        
        default_place = self.place_positions['default']
        
        for i, pick_pos in enumerate(self.pick_positions, 1):
            print(f"\n--- Кубик {i} из {len(self.pick_positions)} ---")
            self.move_single_cube(pick_pos, default_place)
        
        print("\n" + "="*50)
        print("СОРТИРОВКА ЗАВЕРШЕНА!")
        print("="*50)
    
    def sort_by_color(self, colors):
        """
        Сортировка кубиков по цвету
        
        Args:
            colors (list): список цветов для каждого кубика
        """
        print("\n" + "="*50)
        print("НАЧАЛО СОРТИРОВКИ ПО ЦВЕТУ")
        print("="*50)
        
        for i, (pick_pos, color) in enumerate(zip(self.pick_positions, colors), 1):
            print(f"\n--- Кубик {i}: {color.upper()} ---")
            
            if color in self.place_positions:
                place_pos = self.place_positions[color]
            else:
                place_pos = self.place_positions['default']
            
            self.move_single_cube(pick_pos, place_pos)
        
        print("\n" + "="*50)
        print("СОРТИРОВКА ЗАВЕРШЕНА!")
        print("="*50)
    
    def calibrate(self):
        """Режим калибровки - получение координат от пользователя"""
        print("\n" + "="*50)
        print("РЕЖИМ КАЛИБРОВКИ")
        print("="*50)
        print("1. Переключитесь в DobotStudio в режим JOG")
        print("2. С помощью ручного управления подведите захват к точкам")
        print("3. Записывайте координаты, которые показываются в программе")
        print("\nНажмите Enter для продолжения...")
        input()
        
        points = ['подхода к кубику', 'захвата кубика', 'подхода к выгрузке', 'выгрузки']
        for point in points:
            input(f"Подведите робота к точке {point} и нажмите Enter...")
            print("   Введите координаты X, Y, Z через пробел: ", end='')
            try:
                x, y, z = map(float, input().split())
                print(f"   Сохранено: X={x}, Y={y}, Z={z}\n")
            except:
                print("   Ошибка ввода, пропускаем...")

def main():
    """Основная функция программы"""
    print("ПРОГРАММА УПРАВЛЕНИЯ DOBOT MAGICIAN")
    print("Практическая работа №3: Автоматизация сортировки\n")
    
    # Создаем экземпляр сортировщика
    # ВНИМАНИЕ: замените COM3 на ваш реальный порт!
    sorter = DobotSorter(port='COM3')
    
    # Подключаемся к роботу
    if not sorter.connect():
        print("Не удалось подключиться к роботу. Проверьте:")
        print("1. Подключен ли USB-кабель")
        print("2. Включен ли робот")
        print("3. Правильно ли указан COM-порт")
        return
    
    try:
        # Меню выбора режима работы
        print("\nВыберите режим работы:")
        print("1. Перемещение одного кубика (тест)")
        print("2. Сортировка всех кубиков (цикл)")
        print("3. Сортировка по цвету (с условием)")
        print("4. Режим калибровки")
        print("0. Выход")
        
        choice = input("\nВаш выбор (0-4): ").strip()
        
        if choice == '1':
            # Тестовое перемещение одного кубика
            if len(sorter.pick_positions) > 0:
                sorter.move_single_cube(
                    sorter.pick_positions[0], 
                    sorter.place_positions['default']
                )
        
        elif choice == '2':
            # Сортировка всех кубиков
            sorter.sort_all_cubes()
        
        elif choice == '3':
            # Сортировка по цвету
            colors = []
            print("Введите цвета для каждого кубика (red/blue):")
            for i in range(len(sorter.pick_positions)):
                color = input(f"Кубик {i+1}: ").strip().lower()
                colors.append(color if color in ['red', 'blue'] else 'default')
            sorter.sort_by_color(colors)
        
        elif choice == '4':
            # Калибровка
            sorter.calibrate()
        
        else:
            print("Выход из программы")
    
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
    
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
    
    finally:
        # Обязательно отключаемся от робота
        sorter.disconnect()
    
    print("\nРабота программы завершена")

if __name__ == "__main__":
    main()
