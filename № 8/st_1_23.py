import itertools
k=0
l = list(itertools.product('012345678', repeat=7))
for x in l:
    x=''.join(x)
    if x.count('6')==1 and x[0]!='0':
        if x.count('1')+x.count('3')+x.count('5')+x.count('7')==2:
            k+=1
print(k)
