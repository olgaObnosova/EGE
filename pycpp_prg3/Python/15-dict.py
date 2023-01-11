# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 15. Словари
#

wordList = {}
wordList = {"бегемот": 0, "пароход": 2}
print( wordList["пароход"] )

wordList["пароход"] = 1
print( wordList["пароход"] )

wordList["пароход"] += 1
print( wordList["пароход"] )

wordList["полёт"] = wordList.get("полёт",0) + 1
print( wordList["полёт"] )

allKeys = wordList.keys()
print( allKeys )

sortKeys = sorted( wordList.keys() )
print( sortKeys )

sortKeys = sorted( wordList )
print( sortKeys )

for value in wordList.values():
  print( value )

for key, value in wordList.items():
  print( key, "->", value )


