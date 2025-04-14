with open('21408') as f:
    sp=[[int(x) for x in line.split()] for line in f]
k=0
for x in sp:
    nep = set()
    pov = set()
    for i in x:
        if x.count(i)==1:
            nep.add(i)
        else:
            pov.add(i)
    if len(pov)==2 and len(nep)==1 and max(pov)>max(nep):
        k+=1
        print(x)
print(k)

