# -*- coding: utf-8

# Программа № 3. Сортировка слиянием

from random import randint
import time
N = 100000
A =[randint(10,100) for i in range(N)]
timeLast = time.time()# время в секундах начальное
#print(A)

def mergeSort ( A ):
  if len(A) <= 1: return A
  mid = len(A) // 2
  L = mergeSort( A[:mid] )
  R = mergeSort( A[mid:] )
  return merge(L, R)

def merge(A, B):
  C = []
  while A and B:
    if A[0] <= B[0]:
      C.append(A.pop(0))
    else:
      C.append(B.pop(0))
  return C + A + B


A = mergeSort(A)
timeEnd=time.time()# время в секундах конечное
#print(A)
print(timeEnd-timeLast)
