# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 13. Символьные строки, срезы
#

s = "0123456789"
sMiddle = s[3:8]    # sMiddle = "34567"
print( sMiddle )

sMiddle = s[-7:-2]  # sMiddle = "34567"
print( sMiddle )

s = "0123456789"
sFirst = s[:4]    # sFirst = "0123"
sLast = s[-4:]    # sLast = "6789"
print( sFirst )
print( sLast )

sReversed = s[::-1]
print( sReversed )

s = "0123456789"
sEnds = s[:3] + s[9:]  # sEnd = "0129"
print( sEnds )

s = "0123456789"
sABC = s[:3]+"ABC"+s[3:] # sABC = "012ABC3456789"
print( sABC )





