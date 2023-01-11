f=open('4205.txt')
n,m=map(int,f.readline().split())
sp=[]
for line in f:
    sp.append(int(line))
sp.sort()
print(sp[-1])
print(m)
kus=sp.pop()
ost.append(kus)
#while len(ost)>0:
    

    
print(sp)
