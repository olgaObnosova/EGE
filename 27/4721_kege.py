with open('27-B_4721.txt') as f:
    maxx = maxx2 = 0
    n, v, m = map(int, f.readline().split())
    sp = [0]*100084
    for line in f:
        a, b = map(int, line.split())
        sp[a] = b//v + bool(b % v)
for i in range(m, len(sp) - m):
    if sum(sp[i - m:i + m + 1]) > maxx2 and sp[i] != 0:
        maxx2 = sum(sp[i - m:i + m + 1])
        j = i
        maxx = max(sum(sp[i - m:i + m + 1]), maxx)
print(maxx)
#print(j)
#print(sp)
#print(sum(sp[108 - m:108 + m + 1]))
print(sp[j])