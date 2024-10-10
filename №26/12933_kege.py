with open('pr.txt') as f:
    n, k= map(int, f.readline().split())
    sp=[]
    cnt=0
    for x in f:
        cnt+=1
        a, b = map(int, x.split())
        sp.append([a,cnt, 'sh'])
        sp.append([b, cnt, 'okr'])
sp.sort()
tr=[0]*n
prav=n-1
lev=0
c=0
for x in sp:
    if x[1] not in tr:
        if x[-1] == 'okr':
            tr[prav]=x[1]
            prav-=1
        else:
            tr[lev]=x[1]
            c+=1
            lev+=1
print(c, tr[k-1])

