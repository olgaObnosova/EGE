mx=0
for i in range(108,1000,9):
    a=i*'5'
    while '555' in a or '11' in a or '2' in a:
        if '555' in a:
            a=a.replace('555', '1',1)
        if '11' in a:
            a=a.replace('11', '25',1)
        if '2' in a:
            a=a.replace('2', '5',1)
    if int(a)>mx:
        mx=int(a)
        otv=i
print(otv)