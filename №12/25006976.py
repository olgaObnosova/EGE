s=set()
for i in range(1,1000):
    a='8'*i
    while '555' in a or '888' in a:
        a=a.replace('555','88',1)
        a=a.replace('888','55',1)
    s.add(a)
print(len(s))
print(s)
