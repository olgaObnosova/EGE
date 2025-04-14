with open('26st_01_04.txt') as f:
    n=int(f.readline())
    sp=[[int(x) for x in line.split()] for line in f]
vr=[0]*1440
maxx=0
for x in sp:
    st, end = x
    for i in range(st, end+1):
        vr[i]+=1
k=0
for i in range(1440-1):
    if vr[i]==vr[i+1]:
        k+=1
        maxx=max(maxx, k)
    else:
        otv1 = otv
        otv=i
        k=1
print(maxx)
print(otv)
print(vr[-20:])