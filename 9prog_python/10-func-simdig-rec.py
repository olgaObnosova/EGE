# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 10. Функция sumDigits рекурсивная
#

def sumDigRec( n ):
  if n == 0: return 0
  digit = n %10;
  sum1 = sumDigRec( n // 10 )
  return sum1 + digit

print( sumDigRec(35) )
print( sumDigRec(345) )