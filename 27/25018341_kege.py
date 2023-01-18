with open('25018341.txt') as f:
    n = int(f.readline())
    sp = []
    k = 0
    s = 0
    for line in f:
        s += int(line) * k
        k += 1
        sp.append(int(line))
summ = sum(sp)
maxx = 0
suml = 0
for i in range(len(sp)-1):
    suml += sp[i]
    sump = summ - suml
    s = s - sump + suml
    if s > maxx:
        maxx = s
        p = i
print(maxx, p)