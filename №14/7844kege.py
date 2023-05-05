sp='0123456789abcdefghijklmnopqrstuvwxyz'
for p in range(22,37):
    for q in range(32, 37):
        for x in sp[:p]:
            a=int('ale'+x, p)
            b=int('danov',q)
            if (a+b)%2023==0:
                print((a+b)//2023, x)
