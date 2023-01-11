# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 21. Генераторы списков
#

N = 10
A = [i for i in range(N)]
print(A)

A = list(range(N))
print(A)

A = [i*i for i in range(N)]
print(A)

A = [i for i in range(100)
       if i % 7 == 0]
print(A)

A = [i for i in range(100)
       if i % 7 == 0 and i % 10 == 1]
print(A)
