# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 10. Сложение чисел в файле
#

fileName = "input_10.txt"

Fin = open( fileName )
sum = 0
while True:
  s = Fin.readline()
  if not s: break
  sum += int(s)
print(sum)
Fin.close()

sum = 0
for s in open( fileName ):
  sum += int(s)
print(sum)
