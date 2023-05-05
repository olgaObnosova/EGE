for n in range(16080808, 1, -1):
    s1 = 0
    s2 = 0
    for x in str(n):
        if int(x) % 2 != 0:
            s1 += int(x)
    for i in range(len(str(n))):
        if i % 2 != 0:
            s2 += int(str(n)[i])
    r = abs(s1 - s2)
    if r == 29:
        print(n)
