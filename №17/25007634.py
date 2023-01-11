f=open('17_25007634.txt')
sp=[]
for line in f:
    sp.append(int(line))
k=0
maxr=-99999999999
if sp[0]<sp[1]:
    k+=1
    maxr=max(maxr,sp[0]-sp[1])
for i in range(1,len(sp)-1):
    if sp[i-1]>sp[i]<sp[i+1]:
        k+=1
        maxr=max(maxr,max(abs(sp[i]-sp[i-1]),abs(sp[i]-sp[i+1])))
if sp[-1]<sp[-2]:
    k+=1
    maxr=max(maxr,sp[-1]-sp[-2])
print(k, maxr)
    
