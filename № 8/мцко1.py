#https://kompege.ru/variant?kim=25003483
from itertools import *
a=list(permutations('ЛАГЕРЬ',r=6))
count=0
print(a[0])
print(len(a))
for x in a:
    x=''.join(x)
    
    if x[0]!='Ь' and x.count('ЕА')==0:
        count+=1
print(count)
