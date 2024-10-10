import itertools as t
s=list(t.product('0123456',repeat = 6))
k=0
for x in s:
    x=''.join(x)
    if x[0]!='0' and x.count('3')==1:
        x=x.replace('3','1')
        x = x.replace('5', '1')
        if '11' not in x:
            k+=1
print(k)