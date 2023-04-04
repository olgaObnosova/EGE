with open('27B_5036.txt') as f:
    n = int(f.readline())
    sp = []
    s = k = otv = prs = levs = 0
    k2 = n // 2
    for line in f:
        sp.append(int(line))
        s += int(line)
        if k <= n // 2:
            otv += k * int(line)
            k += 1
            levs += int(line)
        else:
            k2 -= 1
            otv += (k2) * int(line)
            prs += int(line)
prs = prs + sp[0]
levs = levs - sp[0]
minn = float('inf')
spis = []
k1 = 0
for i in range(1, len(sp)):
    if i < n // 2:
        otv = otv + prs - levs
        prs += sp[i] - sp[n // 2 + i]
        levs += sp[n // 2 + i] - sp[i]
        # print(otv, prs, levs)
    else:
        prs = s - levs
        otv = otv - levs + prs
        levs += sp[k1] - sp[i]
        k1 += 1
        # print(otv, prs, levs)
    if otv < minn:
        minn = otv
        punkt = i
print(minn, punkt + 1)
