import itertools as t
comb = list(t.product('СПОЛКЙЕДА', repeat=6))
k=0
for x in comb:
    x=''.join(x)
    if k%2==0 and x[0]=='К' and x.count('Й')>=2 and \
            x.count('С')==0 and x.count('Е')==0:
        print(k)
        break
    k+=1