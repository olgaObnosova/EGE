import itertools as t
comb=list(t.product('АВИКПРЧЫ', repeat = 5))
sp=[]
k=1
for x in comb:
    if k%5!=0:
        sp.append(''.join(x))
    k+=1
for i in range(len(sp)):
    if 'А' not in sp[i] and 'И' not in sp[i] and \
            'Ы' not in sp[i] and sp[i].count('В')==1 and \
            sp[i].count('П') == 1 and sp[i].count('К')==1 and \
            sp[i].count('Р') == 1 and sp[i].count('Ч')==1:
        otv=i
        break
print(otv+1)