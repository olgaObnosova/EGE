import string as s
alf = s.digits + s.ascii_lowercase
alf = alf[:29]
print(alf)
for x in alf:
    a = int(f'923{x}874', 29)
    b = int(f'524{x}6152', 29)
    if (a+b)%28==0:
        print(x, (a+b)//28)