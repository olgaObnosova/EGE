# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 39. Динамическое программирование.
#                 Расстояние Левенштейна

def minEditDistance(s1, s2):
  """ Вычисление минимального расстояния редактирования sl->s2."""
  lenl = len(s1)
  len2 = len(s2)
    # Создание двумерной структуры, такой, что m [i][j] = О
    # for i in 0 .. lenl и for j in 0 .. Ien2
  m = [None] * (lenl + 1)
  for i in range(lenl+1):
    m[i] = [0] * (len2+1)

    # Настройка начальных значений по горизонтали и вертикали
  for i in range(1, lenl+1):
    m [i][0] = i
  for j in range(1, len2+1) :
    m[0][j] = j

    # Вычисление наилучших значений
  for i in range(1,lenl+1):
    for j in range(1,len2+1):
      cost = 1
      if s1[i-1] == s2 [ j-1]: cost = 0
      replaceCost = m[i-1][j-1] + cost
      removeCost = m [i-1][j] + 1
      insertCost = m[i][j-1] + 1
      m [i] [j] = min(replaceCost,removeCost,insertCost)

  for i in range(0,lenl+1):
    for j in range(0,len2+1):
       print("%3d" % m[i][j], end="")
    print()

  return m[lenl][len2]

print( minEditDistance("CGADTA", "AGCDATGCAAGT") )
