# -*- coding: utf-8
# Программа № 41. Игра с камнями. Динамическое программирование
#

N = 15
LOSE = -1
WIN = 1
W = [LOSE]*(N+1)
print(W)
for i in range(1,N+1):
  if W[i] == LOSE:       # проигрышная позиция
    for k in range(1,3): # все возможные ходы
      if i+k <= N:       # не выходим за границы
        W[i+k] = WIN

for i in range(N+1):
  if W[i] == WIN:
    print( i, '+')
  else:
    print( i, ":-(" )
