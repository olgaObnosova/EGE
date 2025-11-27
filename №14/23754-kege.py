for x in range(1, 3001):
    a = 9*11**210+8*11**150-x
    k = 0
    while a:
        if a%11==0:
            k+=1
        a=a//11
    if k==60:
        print(x)