import fnmatch as p
k = maxx = 0
with open('5799.txt') as f:
    sp = []
    for line in f:
        sp.append(int(line))
for i in range(len(sp) - 2):
    m = 1
    a = str(sp[i]) + str(sp[i + 1]) + str(sp[i + 2])
    for x in a:
        m *= int(x)
    if m <= 2 * 10 ** 9 and (p.fnmatch(str(m), '43*6*')):
        k += 1
        maxx = max(maxx, m)
print(k, maxx)