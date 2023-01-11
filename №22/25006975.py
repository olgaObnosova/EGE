for i in range(1000, -1,-1):
    d=i
    c=0
    N=0
    T=d
    while N!=144:
        N=N+T
        T=T+d
        c=c+1
        if N>144:
            break
    if c%2!=0:
        c=c+5
        
    if c==8 and N==144:
        print(i)
    
    
