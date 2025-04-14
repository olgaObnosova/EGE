with open('26 (6).txt') as f:
    n=int(f.readline())
    sp=[[int(x) for x in line.split()] for line in f]
print(sp[:5])
vr=[0]*1440
for x in sp:
    st, e = x
    for i in range(st, e):
        vr[i]+=1
maxx= max(vr)
print(maxx)
piki=[]
for i in range(1440):
    if maxx==vr[i]:
        piki.append(i)
print(piki)
