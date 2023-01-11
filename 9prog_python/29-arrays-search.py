# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 29. Линейный поиск
#

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
X = 6
i = 0
while i < N and A[i] != X:
  i += 1

if i < N:
  print( "A[{}]={}".format(i,X) )
else:
  print( "Не нашли!" )

nX = -1
for i in range(N):
  if A[i] == X:
    nX = i
    break

if nX >= 0:
  print( "A[{}]={}".format(i,X) )
else:
  print( "Не нашли!" )

for i in range(N):
  if A[i] == X:
    print( "A[{}]={}".format(i,X) )
    break
else:
  print( "Не нашли!" )

if X in A:
  nX = A.index(X)
  print( "A[{}]={}".format(i,X) )
else:
  print( "Не нашли!" )


