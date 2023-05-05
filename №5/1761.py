for i in range(99, 0, -1):
    n = bin(i)[2:][::-1]
    if int(n, 2) == 9:
        print(i)
