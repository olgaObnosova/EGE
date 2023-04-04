minn = float('inf')
for i in range(1000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '1' + n + '00'
    else:
        n = n + bin(n.count('1'))[2:]
    r = int(n, 2)
    if r > 190:
        if r < minn:
            minn = r
            otv = i
print(otv)
