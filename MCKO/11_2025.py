alf='0123456789ab'
for x in alf:
    a = int(f'154{x}3', 12)
    b = int(f'1{x}365', 12)
    if (a+b)%13==0:
        print(x, (a+b)//13)
