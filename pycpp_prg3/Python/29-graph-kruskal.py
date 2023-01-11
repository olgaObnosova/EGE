# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 29. Графы. Минимальное остовное дерево
#                 Алгоритм Краскала

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

col = [i for i in range(N)]

ostov = []
for k in range(N-1):
    # поиск ребра с минимальным весом
  minDist = 1e10         # очень большое число
  for i in range(N):
    for j in range(N):
      if col[i] != col[j] and W[i][j] < minDist:
        iMin = i
        jMin = j
        minDist = W[i][j]
    # добавление ребра в список выбранных
  ostov.append ( (iMin, jMin) )
    # перекрашивание вершин
  c = col[jMin]
  for i in range(N):
    if col[i] == c:
      col[i] = col[iMin]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for edge in ostov:
  print( "(", letters[edge[0]], ", ",
              letters[edge[1]], ")", sep="" )
