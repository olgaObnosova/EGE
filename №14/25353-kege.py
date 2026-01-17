for x in range(27_001):
    k=0
    a = 3*27**9+2*27**6+27**3-x
    while a:
        if a%27==0:
            k+=1
        a=a//27
    if k==6:
        print(x)
        break