for i in range(1, 5000):
    n = 2 * i
    n = bin(n)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    if int(n, 2) > 249:
        print(i)
