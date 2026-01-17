import string as s
a=s.digits+s.ascii_lowercase
a=a[:27]
for x in a:
    a1 = int(f'472{x}215', 27)
    a2 = int(f'92{x}538', 27)
    if (a1+a2)%26==0:
        print(x, (a1+a2)//26)
for x in range(27):
    a1= 4*27**6+7*27**5+2*27**4+x*27**3+2*27**2+1*27+5
    a2 = 9 * 27 ** 5 + 2 * 27 ** 4 + x * 27 ** 3 + 5 * 27 ** 2 + 3 * 27 + 8
    if (a1+a2)%26==0:
        print(x, (a1+a2)//26)