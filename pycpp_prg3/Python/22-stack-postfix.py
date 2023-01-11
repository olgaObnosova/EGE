# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 22. Вычисление постфиксной формы с помощью стека
#

#data = input().split()				# (1)
s = "5 15 + 4 7 + 1 - /"
data = s.split()

stack = []							  # (2)
for x in data:						# (3)
  if x in "+-*/":					# (4)
    op2 = int( stack.pop() )			# (5)
    op1 = int( stack.pop() )			# (6)
    if   x == "+": res = op1 + op2	# (7)
    elif x == "-": res = op1 - op2	# (8)
    elif x == "*": res = op1 * op2	# (9)
    else:         res = op1 // op2	# (10)
    stack.append( res )				# (11)
  else:
    stack.append( x )				# (12)

print( stack[0] )					# (13)
