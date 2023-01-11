f=open('st2.txt')
sp=[]
k,s=0,0
maxs,count=0,0
for line in f:
    sp.append(int(line))
for x in sp:
    if x%2==0:
        k+=1
        s+=x
sr=s/k
for i in range(len(sp)-1):
    if (sp[i]%3==0 or sp[i+1]%3==0) \
       and(sp[i]<sr or sp[i+1]<sr):
        count+=1
        maxs=max(maxs,(sp[i]+sp[i+1]))
print(maxs)
print(count)
