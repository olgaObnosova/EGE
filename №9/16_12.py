with open('16_12') as f:
    k = 0
    for x in f:
        x=x.split()
        x=[int(i) for i in x]
        if len(set(x))==4:
            pov=[]
            nep=[]
            for y in x:
                if x.count(y)==2:
                    pov.append(y)
                if x.count(y)==1:
                    nep.append(y)
            sr=(min(pov)+max(pov))/2
            if sr<nep[0]:
                k+=1
print(k)
