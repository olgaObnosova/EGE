f=open('25006974A.txt')
n=int(f.readline())
kc,kn=0,0
minc,minn=999999999,99999999
maxch,maxn=0,0
sp=[]
k=0
for line in f:
    #sp.append(int(line))
    a=int(line)
    
    if a%2==0:
        if a>minn:
            k+=kn
        kc+=1
        minc=min(minc,a)
    else:
        if a>minc:
            k+=kc
        kn+=1
        minn=min(minn,a)
print(kc)
print(kn)
print(minc)
print(minn)
#print(sp[-1])
#print(sp[-2])
print(k)
