import  itertools as t
sp=list(t.product(sorted('эльбрус'), repeat = 5))
k=1
for x in sp:
    x=''.join(x)
    if x.count('с')>=2 and x.count('л')==1 \
            and 'ээ' not in x and k%2==0:
        print(x, k)
    k+=1
