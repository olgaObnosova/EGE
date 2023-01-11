# -*- coding: utf-8
# Заливка области с помощью очереди
#
def printPicture(A):
  for y in range(YMAX):
    for x in range(XMAX):
     print( A[x][y], end="" )
    print()
A = [[0,1,0,3,0],
     [1,1,1,3,1],
     [0,1,0,1,1],
     [1,2,2,2,0],
     [1,2,2,2,0]]
XMAX = len(A)
YMAX = len(A[0])

printPicture( A )
print()

NEW_COLOR = 2
x0, y0 = 1, 0
color = A[x0][y0]
Q = [ (x0,y0) ]
while Q:					# (1)
  x, y = Q.pop(0)
  print(Q)# (2)
  if A[x][y] == color:	# (3)
    A[x][y] = NEW_COLOR	# (4)
    if x > 0:      Q.append( (x-1,y) )
    if x < XMAX-1: Q.append( (x+1,y) )
    if y > 0:      Q.append( (x,y-1) )
    if y < YMAX-1: Q.append( (x,y+1) )

printPicture( A )
