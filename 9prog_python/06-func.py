# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 6. Функция average
#

def average( a, b ):
  avg = (a+b)/2
  return avg

average(5, 9)
sred = average(5, 9)
print( sred )

print( average(4, 8) )

a = 5
b = 7
sred = average(a, b+8)
print( sred )

x = 1
y = 2
z = 3
c = 2*average(x, y) + z
print(c)

a = 9
b = 7
x = 12
if average(a, b) > 4:
  print("Свистать всех наверх!")
while average(a,b) < x:
  a += 1
print(a)