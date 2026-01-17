alf = '0123456789abcd'
for p in range(33, 100):
    a=int('kot', p) #100 = 1*p**2+0*p**1+0*p**0
    b=int('golodni', p) #kot = 18*p**2+
    c=int('meeow', p)
    d =int('100', p)
    if a+b==c*d-20194023088:
        print(p)
