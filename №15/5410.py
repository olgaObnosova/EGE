for a in range(1,100):
    f=1
    
    for x in range(100):
        for y in range(100):
            f*=(2*y+x!=70 or x<y or a<x)
    if f:
        print(a)
    
