for a in range(100, 1, -1):
    f = 1
    for x in range(1, 1000):
        f *= (x % a == 0 or x % 23 != 0 or x not in range(50, 71))
    if f:
        print(a)
