# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 22. Вывод массива
#

N = 10
A = [i for i in range(N)]

print(A)

for i in range(N):
  print(A[i])

for x in A:
  print(x, end=" ")
print()

print( *A )