with open('27_6796b.txt') as f:
    n, k = map(int, f.readline().split())
    sp = [int(x) for x in f]
maxx = maxp1 = maxpr = 0
for i in range(n-k*2):
    maxx = max(maxx, sp[i])
    maxp1 = max(maxp1, maxx + sp[i + k])
    maxpr = max(maxpr, maxp1 + sp[i + 2 * k])
print(maxpr)
