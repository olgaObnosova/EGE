import itertools as t
alf='0123456789ab'
c=0
for i in range(2, 13):
    l=list(t.product(alf, repeat = i))
    for x in l:
        f=1
        x=''.join(x)
        for j in range(len(x)-1):
            if x[j]<=x[j+1]:
                f=0
                break
        if f:
            c+=1
print(c)