import itertools as t
comb= list(t.product('АИКЛМЬ', repeat=6))
for x in comb:
    if x[0]=='К' and x[-1]=='Ь' and x.count('А')==1 and \
            x.count('И') == 1 and  x.count('К')==1 and \
            x.count('Л') == 1 and x.count('М')==1 and \
            x.count('Ь') == 1:
        perv=x[::-1]

        if abs(comb.index(perv)-comb.index(x))==26655:
            print(comb.index(x), comb.index(perv))

