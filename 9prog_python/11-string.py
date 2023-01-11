# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 11. Символьные строки
#

s = "Питон"
print( type(s) )
s = input("Введите строку")
n = len(s)
print("Длина строки", n, "символов")

password = input("Введите пароль:")
if password == "sEzAm":
  print("Слушаюсь и повинуюсь!")
else:
  print("No pasaran!")

s1 = "паровоз"
s2 = "пароход"
if s1 < s2:
  print(s1, "<", s2)
elif s1 == s2:
  print(s1, "=", s2)
else:
  print(s1, ">", s2)

hello = "Привет"
name = "Пантелеймон"
greeting  = hello + ", " + name + "!"
print( greeting )

s = "Уа! "*10
print(s)



