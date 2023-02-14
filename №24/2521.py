with open('2521.txt') as f:
    f = f.readline()
    k = 1
b = []
maxx = 0
for i in range(len(f) - 1):
    if f[i] == f[i + 1]:
        k += 1
    else:
        if k > maxx:
            maxx = k
            b.append((maxx, f[i]))
        k = 1
print(k)
print(b)
