k=0
def F(n):
    global k
    if n > 0:
        G(n - 1)
    return k
def G(n):
    global k
    k+=1
    if n > 1:
        k += 1
        F(n - 2)


print(F(13))