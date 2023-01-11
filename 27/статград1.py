f=open('27.txt')
n=int(f.readline())
s=0
k=0
s1=[10**20]*10

ms=0
for line in f:
    line=int(line)
    s+=line
    if line%2!=0:
        k+=1
    if k%10==0:
        ms=s
    elif s1[k%10]!=10**20:
        ms=max(ms,s-s1[k%10])
        print(s, ms)
    s1[k%10]=min(s1[k%10],s)
    print(s1)
    
print(ms)
    
