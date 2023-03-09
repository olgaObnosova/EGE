for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        f *= ((x + a >= 160) \
              or ((x % 7 == 0) <= (x - 17 <= 0)))
    if f:
        print(a)
