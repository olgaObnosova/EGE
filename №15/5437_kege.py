for a in range(1, 100):
    f = 1
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 300):
                f*=((z%115==0 or y%78==0 or x%51==0)<=(x%a==0))
    if f:
        print(a)
