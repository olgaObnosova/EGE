f=open('17st3.txt')
sp=[]
s,k=0,0
count=0
maxs=0
for line in f:
    sp.append(int(line))
for x in sp:
    if x%2==0:
        s+=x
        k+=1
sr=s/k

for i in range(len(sp)-1):
    if (sp[i]%3==0  and sp[i+1]<sr) or (sp[i+1]%3==0  and sp[i]<sr):
        count+=1
        maxs=max(maxs,sp[i]+sp[i+1])
print(count)
print(maxs)
