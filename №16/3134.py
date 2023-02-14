from functools import *
@lru_cache()

def F(n):
    global a
    a.append(n+1)
    F(n-1)
    F(n-3)
    return a
a=[]


for n in range(1,1000):
    F(n)
    if sum(a) > 1000000:
        print(n, sum(a))