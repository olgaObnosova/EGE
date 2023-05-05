minn = 999999
for i in range(1, 1000):
    a = bin(i)[2:]
    otv = i - a.count('0')
    otv = bin(otv)[2:]
    otv = otv[-3:] + otv
    r = int(otv, 2)
    if r > 224:
        minn = min(r, minn)
print(minn)
