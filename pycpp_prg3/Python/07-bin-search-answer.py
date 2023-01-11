# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 6a. Двоичный поиск по ответу
#

from random import randint

def fit ( fontSize, W, H ):
  return fontSize <= 16

W, H = 70, 35

# Линейный поиск
fontSize = 1
while fit( fontSize, W, H ):
  fontSize += 1
print( fontSize-1 )

# Двоичный поиск
L, R = 1, 40        	# начальный отрезок
while L < R-1:
  mid = (L+R) // 2  	# нашли середину
  if not fit( mid, W, H ):
        R = mid      # сжатие отрезка
  else: L = mid

print( L )