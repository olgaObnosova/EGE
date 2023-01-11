f = open('25006983.txt')
sp = []
mmax = 0
mmin = 99999999
c = 0
summin = 99999999999999999999
for i in f:    
    sp.append(int(i))
for k in sp:
    if (k % 2 != 0) and (k > mmax):
        mmax = k
for h in sp:
    if (h % 2 != 0) and (h < mmin):
        mmin = h
esum = mmax + mmin
for j in range(len(sp) - 1):
    if ((sp[j] + sp[j + 1]) % 2 == 0) and ((sp[j] + sp[j + 1]) > esum):
        c += 1
        if (sp[j] + sp[j + 1]) < summin:
            summin = (sp[j] + sp[j + 1])

print(c, summin)
