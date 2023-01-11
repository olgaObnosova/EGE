k=0
d=''
for i in range(3,10):
    s=609
    #k=0
    d=''
    while s>0:
        d=d+str(s%i)
        s=s//i
    d=d[::-1]
    if int(d[0])%2!=int(d[-1])%2:
        k+=i
        print(i)
print(k+10)
        
    
