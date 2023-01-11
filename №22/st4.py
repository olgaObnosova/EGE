for i in range(100000,1000000):
    x=i
    a=1
    b=0
    while x>0:
        d=x%10
        a*=d
        if d>5:
            b+=d
        x=x//10
    if a==6300:
        print(b)
