# -*- coding: utf-8
# Заливка области с помощью очереди
f=open('input.txt')
f2=open('output.txt','w')
A=[]
YMAX, XMAX = map(int,f.readline().split())
x0, y0 = map(int,f.readline().split())
NEW_COLOR = (f.readline().strip())
for line in f:
  A.append(line.split())
count=0 
color = A[x0][y0]
Q = [ (x0,y0) ]
while Q:					
  x, y = Q.pop(0)
  #print(Q)
  if A[x][y] == color:	
    A[x][y] = NEW_COLOR
    count+=1
    if x > 0:      Q.append( (x-1,y) )
    if x < XMAX-1: Q.append( (x+1,y) )
    if y > 0:      Q.append( (x,y-1) )
    if y < YMAX-1: Q.append( (x,y+1) )
f2.write(str(count)+'\n')
for i in range(len(A)):
  d=' '.join(A[i])
  f2.write(d+'\n')
f2.close()  
