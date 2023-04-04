import itertools as t
k=0
sp = list(t.product('012345', repeat=6))
for x in sp:
    x=''.join(x)
    if x[0]!='0' and x.count('2')==1 and '12' not in x and '21' not in x \
            and '32' not in x and '23' not in x \
            and '52' not in x and '25' not in x:
        k+=1
print(k)
