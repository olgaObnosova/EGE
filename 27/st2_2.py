f=open('27-Bst2.txt')
n=int(f.readline())
sp=[2*10**9]*30
s=0
smax=0
count=0
for line in f:
    line=int(line)
    s+=int(line)
    if line>0 and line%2==0:
        count+=1
    if s< sp[count%30]:
        sp[count%30]=s
    if sp[count%30]!=2*10**9:
        smax=max(smax,s-sp[count%30])
print(smax)
