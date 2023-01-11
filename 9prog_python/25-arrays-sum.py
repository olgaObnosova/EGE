# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 25. Сумма элементов массива
#

from random import randint

N = 5
A = [randint(20, 100) for i in range(N)]
print(A)

summa = 0
for i in range(N):
  summa += A[i]
print(summa)

summa = 0
for x in A:
  summa += x
print(summa)

print(sum(A))

product = 1
for x in A:
  product *= x
print(product)

