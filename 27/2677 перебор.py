#2677
f=open('B2677.txt')
a=[]
c=0
k13c, k13n, ch,n,k=0,0,0,0,0
n=int(f.readline())
for line in f:
    a.append(int(line))
print(a[-1])
for i in range(len(a)-5):
    for j in range(i+5,len(a)):
        if (a[i]+a[j])%2!=0 and (a[i]*a[j])%13==0:
            k+=1
    print(i)
print(k)
