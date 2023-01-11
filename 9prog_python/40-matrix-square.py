# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 40. Квадратные матрицы
#

def printMatrix( A ):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print( "{:4d}".format(A[i][j]), end="" )
    print()

N = 6
A = [ [0]*N for i in range(N) ]
for i in range(N):
  for j in range(N):
    A[i][j] = (i+1)*10 + (j+1)
printMatrix( A )

# Главная диагональ
summa = 0
for i in range(N):
  summa += A[i][i]
print(summa)

# Побочная диагональ
summa = 0
for i in range(N):
  summa += A[i][N-1-i]
print(summa)

# Под главной диагональю + главная диагональ
summa = 0
for i in range(N):
  for j in range(i+1):
    summa += A[i][j]
print(summa)

# Переставить 0 и 3  строки
A[0], A[3] = A[3], A[0]
printMatrix( A )
print()

# Переставить 2 и 4  столбцы
for i in range(N):
  A[i][2], A[i][4] = A[i][4], A[i][2]
printMatrix( A )