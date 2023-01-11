from functools import lru_cache
@lru_cache
def F( n):
    global k
    k+=1
    if n >= 1:
        k+=1
        F(n-1)
        F(n-3)
        k+=1
    return(k)
    
k=0
print(F(40))
