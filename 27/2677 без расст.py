f=open('primer_2.txt')
a=[]
c=0
k13c, k13n, ch,n,k=0,0,0,0,0
m=int(f.readline())
#print(n)
for line in f:
    a=int(line)
    if a % 13==0:
        if a%2==0:
            k+=(n+k13n)
            k13c+=1
        else:
            k+=(ch+k13c)
            k13n+=1
    else:
        if a%2==0:
            k+=k13n
            ch+=1
        else:
            k+=k13c
            n+=1
print(k)        
            
            
    
