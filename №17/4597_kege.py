with open('4597_kege.txt') as f:
    sp = []
    minn = float('inf')
    for line in f:
        sp.append(int(line))
        minn = min(minn, int(line))
k = maxx = 0
for i in range(len(sp) - 1):
    if sp[i] % 117 == minn or sp[i + 1] % 117 == minn:
        k += 1
        maxx = max(maxx, sp[i] + sp[i + 1])
print(k)
print(maxx)
