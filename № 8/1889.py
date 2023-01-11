from itertools import *
k=0
a=list(permutations('ВУАЛЬ',r=5))
print(a[0])
for x in a:
    x=''.join(x)
    if x[0]!='Ь' and 'ЬА' not in x and\
       'ЬУ' not in x:
        k+=1
print(k)
