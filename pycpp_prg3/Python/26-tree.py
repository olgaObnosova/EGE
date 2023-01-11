# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 26. Деревья
#

class TNode:
  pass

def node(d, L = None, R = None):
  newNode = TNode()	 	# создаём новый узел
  newNode.data = d   	# данные узла
  newNode.left = L		# левое поддерево
  newNode.right = R		# правое поддерево
  return newNode

def DFS( T ):
  if not T: return
  print( T.data, end=" " )
  DFS( T.left )
  DFS( T.right )

def LKP( T ):
  if not T: return
  LKP( T.left )
  print( T.data, end=" " )
  LKP( T.right )

def LPK( T ):
  if not T: return
  LPK( T.left )
  LPK( T.right )
  print( T.data, end=" " )

def DFS_stack( T ):
  stack = [T]
  while stack:
    V = stack.pop()
    print( V.data, end=" " )
    if V.right:
      stack.append( V.right )
    if V.left:
      stack.append( V.left )
  print()

def BFS( T ):
  queue = [T]
  while queue:
    V = queue.pop(0) # первый элемент очереди
    print( V.data, end=" " )
    if V.left:
      queue.append( V.left )
    if V.right:
      queue.append( V.right )
  print()

T = node("*",
      node("+", node("1"), node("4" )),
      node("-", node("9"), node("5" ))
      )

DFS( T )
print()

DFS_stack( T )

LKP( T )
print()

LPK( T )
print()

BFS( T )
