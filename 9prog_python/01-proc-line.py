# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 1. Процедура. Линия из минусов
#

def printLine10():
  print("----------")

def printLine5():
  print("-----")

def printLine( symbol, n ):
  print( symbol*n )

def triangleО( n ):
  for i in range(1,n+1):
    print( "O"*i )

printLine10()
printLine5()
printLine( '*', 20 )
printLine( "*-*", 10 )

triangleО( 7 )
