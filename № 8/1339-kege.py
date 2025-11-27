import itertools as s
posl = list(s.product('ИНА', repeat=4))
per = list(s.permutations('МАРИ', r=4))
sch = 0
k = 0
sp=[]
for x1 in per:
    for x2 in posl:
        x1 = ''.join(x1)
        x2 = ''.join(x2)
        sp.append(x1+x2)
sp.sort()
ind = sp.index('МАРИАННА')
print(ind+1)