#https://kompege.ru/variant?kim=25003483
from itertools import *
a=list(product('0123456',repeat=7))
b=list(permutations('0123456',r=7))
count=0
print(b[0])
print(a[0])
print(len(a))
for x in a:
    x=''.join(x)
    
    if x[0]!='0' and x[0]!='3' and x[0]!='5' \
       and not('22'in x and '44' in x):
        count+=1
print(count)
