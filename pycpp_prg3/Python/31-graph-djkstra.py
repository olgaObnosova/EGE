# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 31. Графы. Кратчайший путь. Алгоритм Дейкстры
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

INF = 30000
selected = [False]*N
dist = [INF]*N
start = 0
dist[start] = 0

V = start
minDist = 0
while minDist < INF:
  selected[V] = True
    # проверка маршрутов через вершину V
  for j in range(N):
    if dist[V] + W[V][j] < dist[j]:
      dist[j] = dist[V] + W[V][j]
    # поиск новой рабочей вершины: min dist[j]
  minDist = 1e10
  for j in range(N):
    if not selected[j] and dist[j] < minDist:
      minDist = dist[j]
      V = j

print(dist)

final = N - 1

V = final
print( letters[V], "<- ", end="" )
while V != start:
  for i in range(N):
    if i != V and dist[i]+W[i][V] == dist[V]:
      V = i
      break
  print( letters[V], end="" )
  if V != start:
    print( " <- ", end="")
  else:
    print()

print("Общая длина пути: ", dist[final])
