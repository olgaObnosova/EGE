k = maxx = 0
with open('4360.txt') as f:
    sp = [int(x) for x in f]
for i in range(len(sp) - 1):
    a = bin(sp[i])[2:]
    b = bin(sp[i + 1])[2:]
    if (a.count('1') > 5 and a.count('1') % 2 != 0) or \
            (b.count('1') > 5 and b.count('1') % 2 != 0):
        k += 1
        maxx = max(maxx, sp[i] + sp[i + 1])
print(k, maxx)
