for a in range(1,100):
    f=1
    for x in range(1,1000):
        f*=(x%3!=0 or x%2!=0 or x-a>=4)
    if f:
        print(a)