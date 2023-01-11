# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 7. Функция max2
#

def max2( a, b ):
  if a > b:
    maximum = a
  else:
    maximum = b
  return maximum

def max3( a, b, c ):
  return max2(max2(a, b), c)

print( max2(3, 5) )
print( max3(3, 4, 5) )