# -*- coding: utf-8
#
# Модуль bintree.py
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 27. Вычисление арфметических выражений с помощью дерева
#                 с использованием модуля

class TNode:
  pass

def node(d, L = None, R = None):
  newNode = TNode()	 	# создаём новый узел
  newNode.data = d   	        # данные узла
  newNode.left = L		# левое поддерево
  newNode.right = R		# правое поддерево
  return newNode

def makeTree( expr ):
  pos = lastOp( expr )
  if pos < 0:  # создать лист
    Tree = node( expr )
  else:      # создать узел-операцию
    Tree = node( expr[pos] )
    Tree.left = makeTree( expr[:pos] )
    Tree.right = makeTree( expr[pos+1:] )
  return Tree

def priority( op ):
  if op in "+-": return 1
  if op in "*/": return 2
  return 100

def lastOp( expr ):
  minPrt = 50   # любое между 2 и 100
  pos = -1
  for i in range( len(expr) ):
    prt = priority( expr[i] )
    if prt <= minPrt:
      minPrt = prt
      pos = i
  return pos

def doOperation( op, n1, n2 ):
  if   op == "+": return n1 + n2
  elif op == "-": return n1 - n2
  elif op == "*": return n1 * n2
  else:           return n1 // n2

def calcTree( Tree ):
  if not Tree.left:
    return int(Tree.data)
  else:
    n1 = calcTree( Tree.left )
    n2 = calcTree( Tree.right )
    return doOperation(Tree.data, n1, n2)
