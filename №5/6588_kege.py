for i in range(100):
    n = bin(i)[2:]
    n = n.replace('1', '*')
    n = n.replace('0', '1')
    n = n.replace('*', '0')
    n = '1' + n
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    if int(n, 2) > 180:
        print(i)
