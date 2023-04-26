with open('25023734.txt') as f:
    k = int(f.readline())
    n = f.readline()
    sp = []
    for line in f:
        a, b = map(int, line.split())
        sp.append((a, b))
sp.sort()
d = [-1] * k
h = 0
for x in sp:
    st, e = x
    for i in range(k):
        if st > d[i]:
            d[i] = e
            h += 1
            t = i
            break
print(h, t + 1)
