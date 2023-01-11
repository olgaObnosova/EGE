k=0
def F(n):
    global k
    k+=1
    print(id(k))
    if n > 0:    
        F(n-2)
        F(n // 2)
    return k
print(F(7))
print(id(k))
