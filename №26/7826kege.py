with open('26_7826.txt') as f:
    k, n =map(int, f.readline().split())
    sp=[]
    for line in f:
        a,b=map(int,line.split())
        sp.append((a,b))
sp.sort()
print(sp)
attr=[(0,0)]*k
#print(attr)
c=0
for x in sp:
    st, end=x
    fl=1
    ##print(attr)
    for i in range(k):
        if st==attr[i][0]:
            c += 1
            attr[i] = x
            fl=0
    if fl:
        for j in range(k):
            if st>attr[j][1]:
                c+=1
                nom=j
                attr[j]=x
                break

print(c)
print(nom+1)
