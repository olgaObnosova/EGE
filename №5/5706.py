minn = 99999999
for i in range(1, 100):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    r = int(n, 2)
    if r > 40:
        minn = min(minn, i)
print(minn)
