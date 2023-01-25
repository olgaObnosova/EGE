import  itertools as f
spis=[]
sp=list(f.permutations('мари', r =4))
sp2=list(f.product('ина', repeat =4))
for x in sp:
    for y in sp2:
        slovo = ''.join(x) + ''.join(y)
        spis.append(slovo)
spis.sort()
print(spis.index(('марианна')))
