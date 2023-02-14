for i in range(1,20):
    a=15*(i*'1'+i*'5')
    s=0
    while '15' in a:
        a=a.replace('15','8',1)
    for x in a:
        s+=int(x)
    if s==105:
        print(i)
