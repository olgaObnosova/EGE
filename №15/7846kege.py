p=range(13,20)
q=range(17,24)
a=[]
for x in range(1, 1000):
    f= (x in p) or (x in q)  or (x in a)
    if f:
        a.append(x)
print(a)