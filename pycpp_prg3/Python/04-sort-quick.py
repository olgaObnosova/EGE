# -*- coding: utf-8
# Программа № 4. Сортировка Quick sort
#
import random
from random import randint
import time
timeLast = time.time()# время в секундах начальное
N = 1000000
A =[randint(10,100) for i in range(N)]
#print(A)

def qSort ( A ):
  if len(A) <= 1: return A		
  X = random.choice(A)  			
  BL = [b for b in A if b < X]	
  BX = [b for b in A if b == X]	
  BR = [b for b in A if b > X]	
  return qSort(BL)+BX+qSort(BR)	

A = qSort(A)
timeEnd=time.time()# время в секундах конечное
#print(A)
print(timeEnd-timeLast)
