import itertools as t
comb = list(t.product('0123456', repeat =5))
k=0
for x in comb:
    x=''.join(x) #121543
    if x[0]!='0' and x.count('6')==1 and '00' not in x and \
            '11' not in x and'22' not in x and'33' not in x and \
            '44' not in x and'55' not in x and'66' not in x:
        k+=1
print(k)

