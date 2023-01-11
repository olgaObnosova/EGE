# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 8. Функция sumDigits
#

def sumDigits( n ):
  summa = 0
  while n != 0:
    digit = n % 10
    summa += digit
    n = n //10
  return summa

print( sumDigits(35) )
print( sumDigits(345) )