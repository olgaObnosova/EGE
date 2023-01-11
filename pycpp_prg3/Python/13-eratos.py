# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 13. Решето Эратосфена
#

N = 100
A = [True]*(N+1)

k = 2
while k*k <= N:
  if A[k]:
    i = k*k
    while i <= N:
      A[i] = False
      i += k
  k += 1

for i in range(2,N+1):
  if A[i]:
    print( i )

primes = [i for i in range(2,N+1) if A[i] ]
print( primes )
