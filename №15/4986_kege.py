for a in range(1, 100):
    f = 1
    for x in range(1, 1000):
        f *= ((x % a == 0) or ((x % 23 == 0) <= (x not in range(50, 71))))
    if f:
        print(a)
