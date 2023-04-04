maxx = 0
for i in range(100):
    n = bin(i)[2:]
    for i in range(2):
        if n.count('1') % 2 == 0:
            n = '11' + n[2:] + '00'
        else:
            n = '10' + n[2:] + '11'
    n = int(n, 2)
    maxx=max(maxx, n)
print(maxx)
