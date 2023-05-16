with open('25025747(B).txt') as f:
    k = 0
    a = 0
    sp = []
    n, d, t = map(int, f.readline().split())
    for line in f:
        x = int(line)
        if x % d != 0:
            k += 1
        else:
            sp.append(k)
            k = 0
    sp.append(k)
# print(sp)
for i in range(len(sp) - t):
    a += sp[i] * sp[i + t]
print(a)