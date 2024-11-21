import  itertools as t
comb= list(t.product('0123456789ab', repeat=5))
k=0
for x in comb:
    if x[0]!='0' and x.count('7')==1 and \
            x.count('9')+x.count('a')+x.count('b')<=3:
        k+=1
print(k)

