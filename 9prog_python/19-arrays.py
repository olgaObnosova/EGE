# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 19. Массивы
#

A = [1, 3, 4, 23, 5]
print( type(A) )
print( A )
A = [1, 3] + [4, 23] + [5]
print( A )

A = ["Вася","Петя","Коля","Маша","Даша"]
N = len(A)
print( A )
print( N )

N = 10
A = [0]*N
print( A )
