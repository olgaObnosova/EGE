for a in range(100):
    f=1
    for x in range(1000):
        f*=(x&35==0 and x&22==0 or x&15!=0 or x&a!=0)
    if f:
        print(a)
