for i in range(1,300):
    a='1'+i*'2'+2*i*'3'+'1'
    while '11' in a or '22' in a or '33' in a:
        if '11' in a:
            a=a.replace('11','23',1)
        if '22' in a:
            a = a.replace('22', '13', 1)
        if '33' in a:
            a = a.replace('33', '12', 1)
    s=0
    for j in a:
        s+=int(j)
    #print(s, i)

    if s==502:
        print(i)
print(bin(82), bin(96))

