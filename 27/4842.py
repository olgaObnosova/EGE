#4842
f=open('4842A.txt')
zn=[int(x) for x in f.readline().split()]
n=zn[0]; k=zn[1]; d=zn[2]
lenn=0
kos=0
summ=0
maxsum=0
def F(n):
    n=str(n)
    if '1'  not in n: return 1
    else: return 0
s=[[0]*d for i in range(k)]
for i in range(n):
    x=int(f.readline())
    lenn+=1
    if (x<0):
        kos+=F(x)
        print(kos)
    summ+=x
    if (summ%d==0) and (kos%k==0):
        maxsum=max(maxsum,summ)

    if s[kos%k][summ%d]!=0:
        maxsum=max(maxsum,summ-s[kos%k][summ%d])

    s[kos % k][summ % d]=min(s[kos%k][summ%d],summ)
    #print(s)
print(maxsum)
