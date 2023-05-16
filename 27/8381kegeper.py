with open('25025747(A).txt') as f:
    a = 0
    sp = []
    n, d, t = map(int, f.readline().split())
    for line in f:
        sp.append(int(line))
# print(sp,len(sp))
for i in range(len(sp)):
    k = 0
    for j in range(i + 1, len(sp)):
        if sp[i] % d != 0 and sp[j] % d == 0:
            k += 1
        if k == t and sp[j] % d != 0:
            a += 1
        if k > t:
            break

print(a)