with open('26_7096(1).txt') as f:
    n=f.readline()
    sp=list(set([int(x) for x in f]))
sp.sort(reverse=True)
t=sp[0]
k=[sp[0]]
for i in range(1,len(sp)):
    if (t-sp[i])>=11:
        t=sp[i]
        k.append(sp[i])
print(len(k), k[-1])

