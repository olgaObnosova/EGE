# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 32. Графы. Кратчайшие пути. Алгоритм Флойда
#

N = 6
INF = 30000   # "бесконечность", нет связи
W = [
  [0,     2,   4, INF, INF, INF],
  [2,     0,   9,   7, INF, INF],
  [4,     9,   0,   8,   1, INF],
  [INF,   7,   8,   0,   3,   1],
  [INF, INF,   1,   3,   0,   2],
  [INF, INF, INF,   1,   2,   0]
  ]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for k in range(N):
  for i in range(N):
    for j in range(N):
      if W[i][k] + W[k][j] < W[i][j]:
        W[i][j] = W[i][k] + W[k][j]

for i in range(N):
  for j in range(N):
     print( "{:2}".format(W[i][j]), end="")
  print()