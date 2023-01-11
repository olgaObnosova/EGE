# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 21. Реверс массива из файла с помощью стека
#

fileName = "input_21.txt"

stack = []
for s in open( fileName ):
  stack.append( int(s) )

Fout = open("output_20.txt", "w")
while stack:  # пока стек не пуст
  x = stack.pop()
  Fout.write ( str(x) + "\n" )
Fout.close()
