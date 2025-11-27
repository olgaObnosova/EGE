import itertools as t
comb = list(t.product('АКОРСТ', repeat =5))
k=0
for x in comb:
    x = ''.join(x)
    k+=1
    if k%2==0 and x[0] not in 'АСТ' and x.count('О')==2:
        print(k, x)
