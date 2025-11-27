for a in range(100):
    f=1
    for x in range(1000):
        f*=((x&117!=0) and (x&91==0))<=(x&a!=0)
    if f:
        print(a)