p = [x for x in range(25,121)]
q = [x for x in range(54,76)]
a=[]
for i in range(150):
    f=1
    for x in range(150):
        f*=((x in q) <=((((x in p) == (x in q) \
                          or (x not in p)<=(x in a)))))

    if f:
        a.append(i)
print(a)
