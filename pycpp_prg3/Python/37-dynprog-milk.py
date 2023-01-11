# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 37. Динамическое программирование.
#                 Задача о разливе молока

volumes = [1, 5, 6]
MMAX = len(volumes)
N = 10
INF = 30000

# Определение минимального количества бидонов
K = [0]*(N+1)
for i in range(1, N+1):
  K[i] = INF
  for v in volumes:
    if i >= v:
      K[i] = min(K[i], K[i-v])
  K[i] += 1

print( K )
print( K[N] )

# Определение размеров взятых бидонов
vRemained = N
while vRemained:
  for v in volumes:
    if K[vRemained] == K[vRemained-v] + 1:
      print( v, end=" ")
      vRemained -= v
      break
print()



