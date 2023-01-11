# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 6. Двоичный поиск
#

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
L, R = 0, N        	# начальный отрезок
while L < R-1:
  mid = (L+R) // 2  	# нашли середину
  if X < A[mid]:		# сжатие отрезка
        R = mid
  else: L = mid

if A[L] == X:
  print( "A[{}]={}".format(L, X) )
else:
  print( "Не нашли!" )
