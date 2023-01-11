f=open('27-Ast2.txt')
n=f.readline()
count=0
s=0
d=[]
sp=[-9999999]*30
for line in f:
    a=int(line)
    s+=a
    if a>0 and a%2==0:
        count+=1
    if count%30==0:
        d.append(s)
    else:
        
        if  s>sp[count%30]:        
            sp[count%30]=s
        s=0
print(max(d))
print(d)
print(sp)
