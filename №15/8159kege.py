b=range(50,71)
for a in range(100):
    f=1
    for x in range(1000):
        for y in range(1000):
            f*=(2*x+y!=150 or x not in b or a>y)
    if f:
        print(a)
