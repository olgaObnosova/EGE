# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 9. Неизвестное количество строк
#

fileName = "input_9.txt"

Fin = open( fileName )
while True:
  s = Fin.readline()
  if not s: break
  print(s, end="")
print()
Fin.close()

Fin = open( fileName )
allStrings = Fin.readlines()
for s in allStrings:
  print(s, end="")
print()
Fin.close()

with open( fileName ) as Fin:
  for s in Fin:
    print(s, end="")
print()

for s in open( fileName ):
  print(s, end="")
print()
