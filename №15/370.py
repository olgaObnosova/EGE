for a in range(1,100):
    f=1
    for x in range(1,1000):
        f*=((x%a!=0)<= ((x%6==0)<= (x%4!=0)))
    if f:
        print(a)
        
    
