# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 9. Логические функции
#

def even( n ):
  return (n % 2 == 0)

print( even(35) )
print( even(34) )

a = 18
half = 0
if even(a):
  half = a // 2
  print("Половина от", a, "равна", half)
else:
  print(a, "не делится на 2")

x = 96
print(x, "= ", end="")
count = 0
while even(x):
  x = x // 2
  count += 1
print(x, "*2^", count, sep="")
