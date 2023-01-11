# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 36. Динамическое программирование.
#                 Задача о размене монет

def showTable ( p, T, N ):
  print("   ", end="")
  for w in range(N+1):
    print("{:3d}".format(w), end="")
  print()
  for i in range(1,N+3):
    print("---", end="")
  print()
  for i in range(MMAX):
    print( "{:2d}:".format(p[i]), end="" )
    for w in range(N+1):
      print("{:3d}".format(T[i][w]) , end="")
    print()
  print()

p = [1, 2, 5, 10]
MMAX = len(p)
N = 10

T = []
for i in range(MMAX):
  T.append([0]*(N+1))

for i in range(p[0],N+1):
  T[0][i] = 1
for i in range(MMAX):
  T[i][0] = 1
for i in range(1,MMAX):
  for w in range(1,N+1):
    T[i][w] = T[i-1][w]
    if w >= p[i]:
      T[i][w] = T[i][w] + T[i][w-p[i]]

showTable(p, T, N)

print ( "Число вариантов размена:", T[MMAX-1][N] )


