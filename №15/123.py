for A in range(-1000,1000):
    f = 1
    for x in range(1000):
        f *= ((A % 25 == 0) and (((x % 24 != 0) or (x % 75 != 0))\
                                 or (x % A == 0)))

    if f:
        print(A)
