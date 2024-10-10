import itertools as f
k=0
t1=list(f.product('0123456789ab', repeat=5))
for x in t1:
    x=''.join(x)
    if x[0] != '0' and x.count('7') == 1 \
            and x.count('9') + x.count('a') \
            + x.count('b') <= 3:
        k += 1
print(k)
'''
alf='0123456789ab'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    x=x1+x2+x3+x4+x5
                    if x[0]!='0' and x.count('7')==1\
                        and x.count('9')+x.count('a')+x.count('b')<=3:
                        k+=1
print(k)
'''