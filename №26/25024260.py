with open('26(9).txt') as f:
    k = int(f.readline())
    sp = []
    n = int(f.readline())
    for x in f:
        a,b = map(int,x.split())
        sp.append((a,b))
sp.sort()
print(sp)
maxx=0
komn = [0]*k
for x in sp:
    z,v=x
    nom=minn=float('inf')
    for i in range(k):
        if komn[i]<=minn:
            minn=komn[i]
            nom=i
    #print(komn, x, minn)
    maxx = max(maxx,abs(komn[nom]-z))
    komn[nom]=v+31
print(maxx)
print(nom+1)


