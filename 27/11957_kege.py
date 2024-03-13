with open('27-B_11957.txt') as f:
    n, t, k, = map(int, f.readline().split()) #t - диапазон
    sp=[]
    for x in f:
        a, b = map(int, x.split())
        sp.append([a, b])
minn=float('inf')
maxx=0
for i in range(n-t):
    minn=min(sp[i][0], minn)
    maxx=max(sp[i+t][1], maxx)
ka=k//minn
print(maxx*ka-minn*ka)
print(maxx, minn)