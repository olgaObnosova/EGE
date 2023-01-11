#https://kompege.ru/variant?kim=25003483
from itertools import *
a=list(product('ВИШНЯ',repeat=6))
count=0
print(a[0])
print(len(a))
for x in a:
    x=''.join(x)
    
    if x.count('В')<=1 and x[0]!='Ш' and x[-1] not in 'ИЯ':
        count+=1
print(count)
