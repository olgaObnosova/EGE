import math
def stepen(n):
    k=0
    while n>1:
        if n%2==0:
            k+=1
            n=n//2
        else:
            return k        
    return k
f=open('27-B_st_1_23.txt')
n=f.readline()
s=0
sp0=[0]*11
sp1=[0]*11
sp2=[0]*11
for line in f:
    line=int(line)
    t=stepen(line)
    if t>10:
        t=10
    if line%3==0:        
            sp0[t]+=1
    if line%3==1:        
            sp1[t]+=1
    if line%3==2:        
            sp2[t]+=1
for i in range(6):
    for j in range(10-i, 11):
        #print(i,j)
        if i==5 and j==5:
            s+=(sp0[5]*(sp0[j]-1))
        else:
            s+=(sp0[i]*sp0[j])
for i in range(11):
    for j in range(10-i, 11):
        s+=(sp1[i]*sp2[j])
        #print(i,j)
#s+=(math.factorial(sp0[5])//(2*(math.factorial(sp0[5]-2))))
print(s)
print(sp0)
print(sp1)
print(sp2)
