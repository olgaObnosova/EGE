for x in '0123456789ABCD':
    z=f'99658{x}29'
    z1=f'102{x}023'
    z2=int(z, 15)+int(z1, 15)
    if z2%14==0:
        print(z2//14, x)