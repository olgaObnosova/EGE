import itertools as t
comb = list(t.permutations('ПАРИЖАНКА', r =9))
s=set()
for x in comb:
    x=''.join(x) #АААИ
    if 'ААА' not in x \
            and x.count('АА')+x.count('АИ')\
            +x.count('ИА')==1:
        s.add(x)
print(len(s))