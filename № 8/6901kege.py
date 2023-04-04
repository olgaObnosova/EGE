import itertools as t
sp=list(t.product('АБРШ', repeat=5))
k=0
for x in sp:
    x=''.join(x)
    k+=1
    if x.count('Б')+x.count('Р')+x.count('Ш')<=3 \
            and ((x.count('А')==2 and x.count('Б')==1 and x.count('Р')==1and x.count('Ш')==1) or \
                 (x.count('А') == 1 and x.count('Б') == 2 and x.count('Р') == 1 and x.count('Ш') == 1) or \
                 (x.count('А') == 1 and x.count('Б') == 1 and x.count('Р') == 2 and x.count('Ш') == 1) or \
                 (x.count('А') == 1 and x.count('Б') == 1 and x.count('Р') == 1 and x.count('Ш') == 2) ):
        print(k)

