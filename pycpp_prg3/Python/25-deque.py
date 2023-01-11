# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 25. Дек = double-ended queue
#

deque = [1, 2, 3, 4, 5]
print(deque)

for x in range(-1,-6,-1):
  deque.insert( 0, x )
  print(deque)

for x in range(5,10):
  deque.append( x )
  print(deque)

for x in range(5):
  top = deque.pop()
  print(deque)

for x in range(5):
  bottom = deque.pop(0)
  print(deque)
