# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 11. Сортировка массива
#

fileName = "input_11.txt"

A = []
for s in open(fileName):
  A.append( int(s) )

A.sort()

Fout = open( "output_10.txt", "w" )
Fout.write( str(A) + "\n" )
for x in A:
  Fout.write( str(x)+"\n" )
Fout.close()

Fin = open( fileName )
allStrings = Fin.read().split()
A = list( map(int, allStrings) )
Fin.close()

A.sort( reverse=True )

Fout = open( "output_10a.txt", "w" )
Fout.write( str(A) + "\n" )
for x in A:
  Fout.write( str(x)+"\n" )
Fout.close()
