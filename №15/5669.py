for a in range(1, 100):
    f = 1
    for x in range(1, 1000):
        f *= (x not in range(160, 181) or x % 35 != 0 or x % a == 0)
    if f:
        print(a)
