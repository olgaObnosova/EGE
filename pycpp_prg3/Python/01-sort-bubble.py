# -*- coding: utf-8
# Программа № 1. Сортировка пузырьком

from random import randint
import time
timeLast = time.time()# время в секундах начальное
N = 10000
A =[randint(10,100) for i in range(N)]
#print(A)

for i in range(N-1):
  for j in range(N-1-i):
    if A[j]> A[j+1]:
      A[j], A[j+1] = A[j+1], A[j]
#print(A)
timeEnd=time.time()# время в секундах конечное
print(timeEnd-timeLast)
