for a in range(200):
    f=1
    for x in range(1,1000):
        f*=(72%x!=0 or 120%x!=0 or a-x>100)
    if f:
        print(a)
        break
    
    
