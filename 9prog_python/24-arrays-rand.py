# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 24. Заполнение массива случайными числами
#

from random import randint

N = 5
A = [0]*N
for i in range(N):
  A[i] = randint(20, 100)
print(A)

A = [randint(20, 100) for i in range(N)]
print(A)
