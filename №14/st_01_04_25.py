import string as s
alf=s.digits+s.ascii_lowercase
alf=alf[:22]
for x in alf:
    a=int(f'98{x}79641', 22)
    b = int(f'25{x}49', 22)
    c = int(f'63{x}5', 22)
    if (a+b+c)%21==0:
        print((a+b+c)//21, x)