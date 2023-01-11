# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 12. Обработка смешанных данных
#

fileName = "input_12.txt"

Fin = open( fileName )
Fout = open( "output_11.txt", "w" )

while True:
  s = Fin.readline()
  if not s: break
  age = int( s.split(";")[1] )
  if age < 5:
    Fout.write( s )

Fin.close()
Fout.close()

Fin = open( fileName )
Fout = open( "output_11a.txt", "w" )

allStrings = Fin.readlines()
for s in allStrings:
  age = int ( s.split(";")[1] )
  if age < 5:
    Fout.write ( s )

Fin.close()
Fout.close()

Fout = open( "output_11b.txt", "w" )
with open( fileName ) as Fin:
  for s in Fin:
    age = int( s.split(";")[1] )
    if age < 5:
      Fout.write( s )
Fout.close()

Fout = open( "output_11c.txt", "w" )
for s in open( fileName ):
  age = int( s.split(";")[1] )
  if age < 5:
    Fout.write( s )
Fout.close()
