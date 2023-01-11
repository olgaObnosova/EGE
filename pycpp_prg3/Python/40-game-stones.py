# -*- coding: utf-8

# Программа № 40. Игра с камнями. Проигрывает тот, кто взял
#                 последний камень.

def gameOver( N ):
  return (N <= 0)

def isWinPos( N ):
  if gameOver(N):
    return True
  for take in range(1,3):
    if not isWinPos(N-take):
      return True
  return False

N = 15
for startCount in range(N+1):
  if isWinPos(startCount):
    print(startCount, "+")
  else:
    print(startCount, ":-(")
