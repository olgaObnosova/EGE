# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 39. Сумма элементов матрицы
#

import random

N = 3
M = 2
A = [ [0]*M for i in range(N) ]
for i in range(N):
  for j in range(M):
    A[i][j] = random.randint( 0, 150 )
print( A )

summa = 0
for i in range(N):
  for j in range(M):
    summa += A[i][j]
print(summa)

summa = 0
for row in A:
  summa += sum(row)
print(summa)
