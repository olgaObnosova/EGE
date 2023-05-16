with open('26(10).txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[]
    for line in f:
        a,b =map(int, line.split())
        sp.append((a,b))
sp.sort()
kam=[0]*k
kol=0
for x in sp:
    st, end=x
    for i in range(k):
        if st > kam[i]:
            kam[i]=st+end
            kol+=1
            break
print(n-kol)