import  itertools as t
sp=list(t.product('агемнрту', repeat=4))
#sp2=list(t.permutations('агемнрту', r=4))
print(sp[:5])
#print(sp2[:5])
k=0
for x in sp:
    x=''.join(x)
    k+=1
    if x[0]<x[1]<x[2]<x[3] and x.count('а')<=1 \
            and x.count('г')<=1 and x.count('е')<=1 \
            and x.count('м') <= 1 and x.count('н') <= 1 \
            and x.count('р') <= 1 and x.count('т') <= 1 \
            and x.count('у') <= 1:
        print(k)
#
