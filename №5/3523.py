for i in range(1, 1000):
    n = int(str(i) + str(i)[-1])
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    n = int(n, 2)
    if n > 413:
        print(i, n)
