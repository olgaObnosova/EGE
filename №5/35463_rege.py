for j in range(100, 1000):
    n=bin(j)[2:]
    for i in range(3):
        k0 = n.count('0')
        k1 = n.count('1')
        if k0 == k1:
            n = n + n[-1]
        elif k0 < k1:
            n = n + '0'
        else:
            n = n + '1'
    r = int(n, 2)
    if r % 4 == 0:
        print(j)
