for a in range(100):
    f=1
    for x in range(1000):
        f*=(x%4==3 and x%6==1 or x%36!=a)
    if f:
        print(a)
        break
