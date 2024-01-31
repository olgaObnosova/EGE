for a in range(1,100):
    f=1
    for x in range(1, 1000):
        f*=(x&a==0) or x&37!=0 or x&12!=0
    if f:
        print(a)