for a in range(250,100,-1):
    f=1
    for x in range(250):
        for y in range(250):
            f*=(x*y> a+13) or (28*y>520) or (x*25>800)
    if f:
        print(a)