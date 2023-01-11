# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 31. Поиск максимума из отрицательных элементов
#

from random import randint

N = 10
A = [randint(-20,200) for i in range(N)]
print(A)

M = -21
for x in A:
  if x < 0 and x > M:
      M = x
if M == -21:
  print( "Нет отрицательных!" )
else:
  print( M )

M = A[0]
for x in A:
  if x < 0:
    if M >=0 or x > M:
      M = x
if M >= 0:
  print( "Нет отрицательных!" )
else:
  print( M )

count = 0
for x in A:
  if x < 0:
    if count == 0 or x > M:
      M = x
    count += 1
if count == 0:
  print( "Нет отрицательных!" )
else:
  print( M )

B = [x for x in A if x < 0]
if B:
  print( max(B) )
else:
  print( "Нет отрицательных!" )

