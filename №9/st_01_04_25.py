with open('st_01_04_25') as f:
    sp=[[int(x) for x in line.split()] for line in f]
k=1
for x in sp:
    pov=[]
    povt=[]
    nepovt=[]
    for i in x:
        pov.append(x.count(i))
        if x.count(i)==1:
            nepovt.append(i)
        else:
            povt.append(i)
    #print(pov)
    if pov.count(2)==6 and pov.count(1)==2:
        if (max(povt)-min(povt))**2>2*sum([x**2 for x in nepovt]):
            print(k)
    k+=1


