for i in range(1,100):
    x=i
    s=0
    a=27**7-3**11+36-x
    while a>0:
        s+=a%3
        a=a//3
    if s==22:
        print(i)
    
