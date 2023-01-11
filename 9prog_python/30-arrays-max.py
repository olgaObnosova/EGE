# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 30. Поиск максимума в массиве
#

from random import randint

N = 10
A = [randint(20,100) for i in range(N)]
print(A)

M = A[0]
for i in range(1,N):
  if A[i] > M:
    M = A[i]
print( M )

M = A[0]
nMax = 0
for i in range(1,N):
  if A[i] > M:
    M = A[i]
    nMax = i
print( "A[{}]={}".format(nMax, M) )

nMax = 0
for i in range(1,N):
  if A[i] > A[nMax]:
    nMax = i
print( "A[{}]={}".format(nMax, A[nMax]) )

M = max(A)
nMax = A.index(M)
print( "A[{}]={}".format(nMax, M) )
