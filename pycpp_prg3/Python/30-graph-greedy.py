# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 30. Графы. Кратчайший путь. Жадный алгоритм
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
prev = -1
current = 0
final = 5
total = 0
visited = [False]*N
visited[current] = True
while current != final:
   minDist = 1e10
   prev = current
   for i in range(N):
      if not visited[i] and W[prev][i] < minDist:
         minDist = W[prev][i]
         current = i
   visited[current] = True
   total += W[prev][current]
   print( "(", letters[prev], ", ",
               letters[current], ")", sep="" )

print("Общая длина пути: ", total)