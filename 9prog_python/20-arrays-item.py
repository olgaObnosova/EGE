# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 20. Обращение к элементу массива
#

A = [3, 2, 7,	0,	5]
i = 1
print(A[i], A[i+1], A[3*i+1], A[A[3*i]])
print(A[1], A[2], A[4], A[0])

N = 10
A = [0]*N
for i in range(N):
  A[i] = i
print(A)

for i in range(N):
  A[i] = N - i
print(A)

for i in range(N):
  A[i] += 1
print(A)


