with open('4705_kege.txt') as f:
    sp = []
    maxx = -10_000
    maxxs = -10_00**2
    k = 0
    for line in f:
        sp.append(int(line))
        if abs(int(line)) % 10 == 3:
            maxx = max(maxx, int(line))
#print(maxx)
for i in range(len(sp) - 1):
    if ((abs(sp[i]) % 10 == 3 and abs(sp[i + 1]) % 10 != 3) \
            or (abs(sp[i + 1]) % 10 == 3 and abs(sp[i]) % 10 != 3)) \
            and sp[i] ** 2 + sp[i + 1] ** 2 >= maxx**2:
        k += 1
        maxxs = max(maxxs, sp[i] ** 2 + sp[i + 1] ** 2)
print(k)
print(maxxs)
