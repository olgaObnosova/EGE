for a in range (1,100):
    f=1
    for x in range(1,10000):
        f*=(x&34!=0 or x&36==0 or x&a!=0)
    if f:
        print(a)
