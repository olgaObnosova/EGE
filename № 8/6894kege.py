import itertools as t
k=0
sp=list(t.product('АЛПЦЯ', repeat=5))
for x in sp:
    k+=1
    x=''.join(x)
    if x.count('А')<2 and x.count('Ц')==2 and x.count('Л')==0:
        print(k)
        break