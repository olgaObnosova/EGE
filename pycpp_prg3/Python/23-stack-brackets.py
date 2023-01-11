# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 23. Проверка скобочного выражения
#

s = "()[{}]"

pair = {"(": ")", "[": "]", "{": "}"}
stack = []
valid = True
for c in s:						    # (1)
  if c in "([{":					# (2)
    stack.append( pair[c] );		# (3)
  elif c in ")]}":				# (4)
    if not stack or c != stack.pop(): 	# (5)
      valid = False		  	# (6)
      break						    # (7)
if stack: valid = False

if valid:
  print("Выражение правильное.")
else:
  print("Выражение неправильное.")
