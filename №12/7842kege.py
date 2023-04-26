for i in range(4, 100):
    a='3'+i*'5'
    while '25' in a or '355' in a or '555' in a:
        if '25' in a:
            a=a.replace('25','32',1)
        if '355' in a:
            a=a.replace('355','25',1)
        if '555' in a:
            a=a.replace('555','3',1)
    if a.count('2')==5:
        print(i)