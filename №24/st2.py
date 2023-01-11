f=open('st2.txt').readline()
sp=[]
maxs=0
k=0
for line in f:
    if line!='A':
        if line=='E':
            k+=1
        sp.append(line)
    elif k>=3:
        maxs=max(maxs,len(sp))
        sp=[]
    else:
        sp=[]
print(maxs)   
