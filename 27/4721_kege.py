with open('27-A_4721.txt') as f:
    maxx = 0
    n, v, m = map(int, f.readline().split())
    sp = [0]*100084
    for line in f:
        a, b = map(int, line.split())
        sp[a] = b//v + bool(b % v)
for i in range(m, len(sp) - m):
    if sp[i] != 0 and sum(sp[i - m:i + m + 1]) > maxx:
        maxx = max(sum(sp[i - m:i + m + 1]), maxx)
        r = i
print(maxx, r)
