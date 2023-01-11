# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 36. Рекурсия с мемоизацией.
#                 Задача о размене монет

cache = {}
def razmen(p, i, W):
  if W < 0: return 0
  if i == 1  or  W == 1: return 1
  if (i,W) in cache:
    return cache[(i,W)]
  cache[(i,W)] = razmen(p, i-1, W) + razmen(p, i, W-p[i])
  return cache[(i,W)]

p = [0, 1, 2, 5, 10]
MMAX = len(p)
N = 10
T = [0]*(N+1)
for w in range(N+1):
  T[w] = razmen(p, MMAX-1, w)

print( T )
print( "Число вариантов размена:", T[N] )


