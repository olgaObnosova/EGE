import itertools as t
s=list(t.product('0123456789AB', repeat=4))
k=0
for x in s:
    x=''.join(x)
    if int(x,12)>1728:
        k+=1
print(k)
print(65*16384/1024)
