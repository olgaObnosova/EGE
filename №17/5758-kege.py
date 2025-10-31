with open('17_5758.txt') as f:
    sp=[int(x) for x in f]
ch = set(sp)
maxx=0
for x in ch:
    t = sp.count(x)
    if t>maxx:
        maxx=t
        otv = x
for i in range(len(sp)):
    for j in range(i+1, len(sp)):
        if min(sp[i], sp[j])<otv<max(sp[i], sp[j]):

