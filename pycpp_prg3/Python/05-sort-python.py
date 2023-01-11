# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 5. Сортировка встроенными средствами
#

from random import randint

N = 10
A =[randint(10,100) for i in range(N)]
print(A)

B = sorted(A)
print(B)
A.sort()
print(A)

B = sorted( A, reverse=True )
print(B)
A.sort(reverse=True)
print(A)

def lastDigit( n ):
  return n % 10

B = sorted( A, key = lastDigit )
print(B)

B = sorted( A, key = lastDigit, reverse=True )
print(B)

B = sorted( A, key = lambda x: x % 10 )
print(B)
A.sort( key = lambda x: x % 10, reverse=True )
print(A)
