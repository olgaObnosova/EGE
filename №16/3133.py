def F( n ):
    global s
    s+=(n+1)
    if n > 1:
        s+=(n+5)
        F(n-1)
        F(n-2)
    return s

for i in range(1000):
    s=0
    h=F(i)
    if h>1000000:
        print(i,s)
        break
