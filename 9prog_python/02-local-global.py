# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 2. Локальные и глобальные переменные
#

def show():
  print( "Global:", i )

def showLocal():
  i = 2
  print( "Local:", i )

def showGlobal():
  global i
  i = 2
  print( "Global:", i )

i = 5
show()
showLocal()
show()
showGlobal()
show()
