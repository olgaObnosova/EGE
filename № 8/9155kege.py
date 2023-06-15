import itertools as t
l=list(t.product('ЬРПЛЕА', repeat=5))
k=0
for i in range(388):
    if l[i][-1]=='Ь':
        k+=1
print(k)