# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 38. Печать матрицы
#

import random

def printMatrix( A ):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print( "{:4d}".format(A[i][j]), end="" )
    print()

def printMatrix2 ( A ):
  for row in A:
    for x in row:
      print( "{:4}".format(x), end="" )
    print()

N = 3
M = 2
A = [ [0]*M for i in range(N) ]
for i in range(N):
  for j in range(M):
    A[i][j] = random.randint( 0, 150 )

print( A )
print()
printMatrix( A )
print()
printMatrix2( A )

