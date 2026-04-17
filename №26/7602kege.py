with open('25023734.txt') as f:
    k = int(f.readline())
    n = f.readline()
    sp = []
    for line in f: # 1 3
        a, b = line.split()
        sp.append((int(a), int(b)))
sp.sort()
d = [-1] * k
h = 0
for x in sp: #[(1,2), (3, 10)]
    st, e = x
    for i in range(k):
        if st > d[i]:
            d[i] = e
            h += 1
            t = i #0
            break
print(h, t + 1)