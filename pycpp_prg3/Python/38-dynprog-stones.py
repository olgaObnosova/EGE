# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 38. Динамическое программирование.
#                 Деление кучи камней на две равных

def showTable ( p, T ):
  print ( "   ", end="");
  for w in range(WMAX+1):
    print ( "{:3d}".format(w), end="")
  print("\n---", end="")
  for i in range(WMAX+1):
    print("---", end="")
  print()
  for i in range(NStones):
    print( "{:2d}:".format(p[i]), end="");
    for w in range(WMAX+1):
      print( "{:3d}".format(T[i][w]), end="" )
    print()
  print()

p = [2, 4, 5, 7]
NStones = len(p)
WMAX = 8

T = []
for i in range(NStones):
  T.append([0] * (WMAX + 1))
for w in range(p[0],WMAX+1):
  T[0][w] = p[0]

for i in range(1,NStones):
  for w in range(1,WMAX+1):
    t0 = T[i-1][w]
    if w >= p[i]:
      t1 = T[i-1][w-p[i]] + p[i]
      T[i][w] = max(t0, t1)
    else:
      T[i][w] = t0

showTable( p, T )

print("Оптимальное решение: w =", T[NStones-1][WMAX] )
print("Берем камни: ");

i = NStones-1
w = WMAX
wRemained = T[NStones-1][WMAX]
while wRemained > 0:
  while i >= 0 and T[i][w] == wRemained:
    i -= 1
  if i < 0:
    print ( wRemained )
    break;
  print ( p[i+1], ' ', end="");
  wRemained -= p[i+1]
  w = wRemained



