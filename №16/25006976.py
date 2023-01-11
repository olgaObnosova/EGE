s=0
def f(n):
    global s
    s+=2*n+1
    if n>1:
        s+=3*n-8
        f(n-1)
        f(n-4)
    return s
print(f(50))
