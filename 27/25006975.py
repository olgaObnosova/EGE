f=open('25006975A.txt')
n=int(f.readline())
sp=[10**9]*69
spk=[00*5]*69
s=0
k=0
mink=9999999999
maxx=0
for line in f:
    line=int(line)
    s+=line
    k+=1
    if s%69==0:
        maxx=max(maxx,s)
        mink=k
    elif sp[s%69]!=10001:
        maxx=max(s-sp[s%69],maxx)
        mink=min(k-spk[s%69],mink)
    sp[s%69]=min(sp[s%69],s)
    spk[s%69]=max(spk[s%69],k)
print(maxx)
print(k)
#print(sp)
