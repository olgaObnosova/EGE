def conv(n, b): #10716
    n=n[::-1]
    s=0
    for i in range(len(n)):
        s+=n[i]*b**i
    return s
for x in range(150):
    a=conv([5,1,x,2,9], 150)
    b=conv([x,0,2,3], 150)
    if (a+b)%149==0:
        print((a+b)//149, x)