minn=9999999
for i in range(1, 100):
    n = bin(i)[2:]
    s = n.count('1')
    n = n + str(s%2)
    s = n.count('1')
    n = n + str(s % 2)
    r = int(n, 2)
    if r >123:
        minn=min(minn, r)
print(minn)