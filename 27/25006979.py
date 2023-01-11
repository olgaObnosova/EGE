f=open('25006979B.txt')
n=int(f.readline())
kc=[0]*13
kn=[0]*13
s=0
for line in f:
    line=int(line)
    if line%2==0:
        s+=(kc[line%13]+kn[line%13])
        kc[line%13]+=1
    else:
        kn[line%13]+=1
        s+=kc[line%13]    
print(kc,kn)
print(s)
    
