maxx=0
for n in range(4, 10_000):
    a='3'+n*'5'
    while'333' in a or '555' in a:
        if '555' in a:
            a=a.replace('555', '3',1)
        else:
            a = a.replace('333', '5', 1)
    s=0
    for x in a:
        s+= int(x)
    if s>maxx:
        maxx=s
        otv=a
print(maxx)
print(otv)