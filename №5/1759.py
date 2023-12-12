for i in range(1,257):
    n = bin(i)[2:]
    n = n.replace('0', '2')
    n = n.replace('1', '0')
    n = n.replace('2', '1')
    n = int(n, 2)
    r = n-i
    if r==-21:
        print(i)
