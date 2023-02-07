for i in range(499, -1, -1):
    n = bin(i)[2:]
    for j in range(3):
        k1 = n.count('1')
        k0 = n.count('0')
        if k0 == k1:
            n = n + n[-1]
        elif k0 < k1:
            n = n + '0'
        else:
            n = n + '1'
    if int(n, 2) % 4 == 0 and int(n, 2) % 8 != 0:
        print(i)
