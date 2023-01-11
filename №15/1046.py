for a in range(1,100):
    f=1
    for x in range(1,100):
        for y in range(1,100):
        
            f*=((3*y+x<a) or (x>12) or (y>15))
    if f:
        print(a)
        
    
