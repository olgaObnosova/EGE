count=0
for i in range(2**20,1,-1):
    x=i
    a=0
    b=0
    m=0
    d=2
    while x>0:
        b=b+1
        if x%2==d:
            a=a+1
        else:
            if a>m:
                m=a
            a=1
            d=x%2
        x=x//2
    if a>m:
        m=a
    if b==20 and m==15:
        count+=1
print(count)
