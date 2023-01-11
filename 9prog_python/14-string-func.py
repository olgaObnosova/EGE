# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 14. Символьные строки, функции
#

s = "aAbBcC"
sUp = s.upper()   # sUp = "AABBCC"
sLow = s.lower()  # sLow = "aabbcc"
print( sUp )
print( sLow )

sWow = "Wow!".upper()    # "WOW!"
print( sWow )

a = 5
b = 4
print( "{}+{}={}".format(a,b,a+b) )

s = "ab1c"
print( s.isdigit() )  # False
s = "123"
print( s.isdigit() )  # True

sRaw = "   Python & C++    "
sClear = sRaw.strip()  # sClear = "Python & C++"
print( sClear )





