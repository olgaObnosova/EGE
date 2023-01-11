# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 26. Подсчёт нужных элементов массива
#

from random import randint

N = 10
A = [randint(20, 100) for i in range(N)]
print(A)

count = 0
for i in range(N):
  if A[i] % 2 == 0:
    count += 1       # увеличить счётчик
print(count)

count = 0
for x in A:
  if x % 2 == 0:
    count += 1
print(count)

B = [x for x in A
       if x % 2 == 0]
print( len(B) )


