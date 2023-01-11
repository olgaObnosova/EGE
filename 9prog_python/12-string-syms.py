# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 12. Символьные строки, работа с символами
#

hello = "Привет!"
print( hello[1] )                # р
print( hello[-6] )               # р

print( hello[5]+hello[2]+"к" )   # тик
print( hello[-2]+hello[-5]+"к" ) # тик

s = "Moscow"
for i in range(len(s)):
  print( s[i], ord(s[i]) )

for c in s:
  print( c, ord(c) )

# s = input( "Введите строку: " )
s = "Пэрэмэна"
sNew = ""
for c in s:
  if c == "э": c = "е"
  sNew += c
print ( sNew )


