for a in range(500):
    f = 0
    for x in range(500):
        for y in range(500):
            f += not((x < 7) or (y >= 5 * x + a - 60) or (x >= 36) or (y<225))
    if f==0:
        print(a)