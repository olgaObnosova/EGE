b = range(50,71)
for a in range(1,500):
    f = 1
    for x in range(1,1000):
        f*=(x%a==0 or x not in b or x%16!=0)
    if f:
        print(a)