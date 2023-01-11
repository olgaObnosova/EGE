# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 37. Матрицы
#

import random

A = [[-1, 0, 1],
     [-1, 0, 1],
     [0, 1, -1]]
print( A )

A = [[-1, 0, 1], [-1, 0, 1], [0, 1, -1]]
print( A )

N = 3
M = 2
A = []
for i in range(N):
  A.append( [0]*M )
print( A )

A = [ [0]*M for i in range(N) ]
print( A )

A = [ [0]*M for i in range(N) ]
for i in range(N):
  for j in range(M):
    A[i][j] = random.randint( 20, 80 )
print( A )
