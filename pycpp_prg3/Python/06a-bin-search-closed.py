# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 6a. Двоичный поиск в замкнутом интервале
#                 X \in [L, R]

from random import randint

N = 10
A =[randint(0,5) for i in range(N)]
A.sort()
print(A)

# Линейный поиск
X = 2
i = 0
while i < N and A[i] != X:
  i += 1
if i < N:
  print( "A[{}]={}".format(i,X) )
else:
  print( "Не нашли!" )

# Двоичный поиск
L, R = 0, N-1        	# начальный отрезок
while L <= R:
  mid = (L+R) // 2  	# нашли середину
  if A[mid] == X: break
  if X < A[mid]:		# сжатие отрезка
        R = mid - 1
  else: L = mid + 1

if L <= R:
  print( "A[{}]={}".format(mid, X) )
else:
  print( "Не нашли!" )
