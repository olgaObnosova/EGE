minn=float('inf')
for i in range(50000):
    n = bin(i)[2:]
    if n[-1] == '0':
        n = n[:-1] + '1'
    else:
        n = n[:-1] + '0'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    n = int(n, 2)
    if n > 78:
        if n<minn:
            minn=n
            otv=i
print(otv)