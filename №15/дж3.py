for a in range(1,100):
    f=1
    for x in range(1, 500):
        for y in range(500):
            f*=(2*x+3*y!=150 or x<a and y<a)
    if f:
        print(a)
        break
