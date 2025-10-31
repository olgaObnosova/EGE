import itertools as t
comb=t.product('012345',repeat=5)
k=0
for x in comb:
    x=''.join(x)
    if x[0]!='0':
        x=x.replace('0','@')
        x = x.replace('2', '@')
        x = x.replace('4', '@')
        x = x.replace('1', '%')
        x = x.replace('3', '%')
        x = x.replace('5', '%')
        if x.count('@@')==0 and x.count('%%')==0:
            k+=1
print(k)