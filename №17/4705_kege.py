with open('4705_kege.txt') as f:
    sp = []
    maxx = -10_000
    maxxs = k = 0
    for line in f:
        sp.append(int(line))
        if int(line) % 10 == 3:
            maxx = max(maxx, int(line))
for i in range(len(sp) - 1):
    if (sp[i] % 10 == 3 and sp[i + 1] % 10 != 3) \
            or (sp[i + 1] % 10 == 3 and sp[i] % 10 != 3) \
            and sp[i] ** 2 + sp[i + 1] ** 2 >= maxx:
        k += 1
        maxxs = max(maxxs, sp[i] ** 2 + sp[i + 1] ** 2)
print(k)
print(maxxs)
