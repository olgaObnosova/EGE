# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 28. Копирование списков
#

import copy

A = [1, 2, 3]
B = A
print(A, B)

A[0] = 0
print(A, B)

A = [1, 2, 3]
B = A[:]
print(A, B)

A[0] = 0
print(A, B)

A = [1, 2, 3]
B = A.copy()
print(A, B)

A[0] = 0
print(A, B)
