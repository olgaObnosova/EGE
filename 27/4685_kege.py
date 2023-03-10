with open('27B_4685.txt') as f:
    n, r = map(int, f.readline().split())
    sp = []
    for line in f:
        sp.append(int(line) // 6 + bool(int(line) % 6))
#print(sp)
otv = []
for i in range(r, len(sp)):
    otv.append(sum(sp[i - r: i + r + 1]))
#print(otv)
maxx = max(otv)
b = otv.index(maxx)
maxx2 = 0
for i in range(len(otv)):
    if otv[i] > maxx2 and maxx2 < maxx and otv[i] != maxx and  abs(b-i) > 2 * r:
        maxx2 = otv[i]

print(maxx + maxx2)
print(otv.index(maxx), otv.index(maxx2))