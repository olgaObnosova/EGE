# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 34. Динамическое программирование. Числа Фибоначчи
#

import time

def fibRec( N ):
  if N < 3: return 1
  return fibRec(N-1) + fibRec(N-2)

Fib = {1: 1, 2: 1}  # F[1]=1, F[2]=1
def fibMemo( N ):
  if N in Fib:                         # (1)
    return Fib[N]                      # (2)
  Fib[N] = fibMemo(N-1) + fibMemo(N-2) # (3)
  return Fib[N]                        # (4)

def fibArray( N ):
  F = [1]*(N+1)
  for i in range(3,N+1):
    F[i] = F[i-1] + F[i-2]
  return F[N]

def fib( N ):
  F1, F2 = 1, 1
  for i in range(3,N+1):
    F2,F1 = F1 + F2, F2
  return F2

N = 33
K = 100000

start_time = time.time()
f = fibRec(N)
print("fibRec: --- %s seconds ---" % (time.time() - start_time))
print(f)

start_time = time.time()
for i in range(K):
  Fib = {1: 1, 2: 1}
  f = fibMemo(N)
print("fibMemo: --- %s seconds ---" % ((time.time() - start_time)/K) )
print(f)

start_time = time.time()
for i in range(K):
  f = fibArray(N)
print("fibArray: --- %s seconds ---" % ((time.time() - start_time)/K) )
print(f)

start_time = time.time()
for i in range(K):
  f = fib(N)
print("fib: --- %s seconds ---" % ((time.time() - start_time)/K) )
print(f)
