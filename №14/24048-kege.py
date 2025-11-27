for p in range(33, 37):
    a=int('kot', p) #100 = 1*p**2+0*p**1+0*p**0
    b=int('golodni', p)
    c=int('meeow', p)
    d =int('100', p)
    if a+b==c*d-20194023088:
        print(p)
