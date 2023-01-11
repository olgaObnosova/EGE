for a in range(1,50):
    f=1
    #for r in range(1,1000):
    for x in range(1,1000):
        f*=((x&108!=0 and x&60!=0) or x&a==0 )
    if f:
        print(a)
    
