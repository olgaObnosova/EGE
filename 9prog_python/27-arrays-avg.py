# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 26. Подсчёт нужных элементов массива
#

from random import randint

N = 10
A = [randint(170, 200) for i in range(N)]
print(A)

count = 0
summa = 0
for x in A:
  if x > 180:
    count += 1
    summa += x
print(summa/count)

B = [x for x in A if x > 180]
print( sum(B)/len(B) )

