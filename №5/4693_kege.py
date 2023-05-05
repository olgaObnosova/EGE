minn = float('inf')
for i in range(1000):
    a = bin(i)[2:]
    if a.count('1') % 2 == 0:
        a = '10' + a[2:] + '0'
    else:
        a = '11' + a[2:] + '1'
    if int(a, 2) > 40:
        minn = min(minn, i)
print(minn)
