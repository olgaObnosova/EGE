for x in '0123456789abc':
    a=f'753{x}2'
    b=f'2{x}173'
    if (int(a,13)+int(b,13))%12==0:
        print((int(a,13)+int(b,13))//12, x)
