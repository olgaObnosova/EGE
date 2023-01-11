for a in range(100):
    f=1
    for x in range(1,1000):
        f*=((x&26==0 and x&13==0) or x&29!=0 or x&a!=0)
    if f:
        print(a)
        break
