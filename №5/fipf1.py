minn = float('inf')
for i in range(100):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + '11'
    r = int(n, 2)
    if r > 225:
        # print(r)
        minn = min(minn, r)
print(minn)
