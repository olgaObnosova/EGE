b=range(50,71)
for a in range(1000, -1,-1):
    f=1
    for x in range(250):
        for y in range(250):
            f*=(2*x+y!=150 or x not in b or a>y)
    if f:
        print(a)
