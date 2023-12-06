for a in range(100, 1, -1):
    f=1
    for x in range(1000):
        for y in range(1000):
            f*=((x+2*y<=48) and (y<=x) and (x+3*y>=a))
    if f:
        print(a)
        break

