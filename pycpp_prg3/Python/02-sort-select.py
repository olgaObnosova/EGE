# -*- coding: utf-8
# Программа № 2. Сортировка выбором минимального элемента
#

from random import randint
import time
timeLast = time.time()# время в секундах начальное
N = 100000
A =[randint(10,100) for i in range(N)]
#print(A)

for i in range(N-1):
 nMin = i
 for j in range(i+1,N):
  if A[j] < A[nMin]: nMin = j
  if nMin != i:
     A[i], A[nMin] = A[nMin], A[i]
timeEnd=time.time()# время в секундах конечное
print(timeEnd-timeLast)

#print(A)
