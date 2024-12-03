a=str(int(input()))
if len(a)==7:
    a=a+a[0]
    a=a[::-1]
    sp='OIZE!SbJ#P'
    n=''
    for x in a:
        n+=sp[int(x)]
    print(n)
else:
    print('WRONG')