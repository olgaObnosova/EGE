with open('27_A_17538.txt') as f:
    n=int(f.readline())
    sp=[]
    sps=[0]
    mins1 = float('inf')
    M = 0
    L = 0
    mins2 = float('inf')

    k=0
    maxs=-float('inf')
    for x in f:
        sp.append(int(x))
        if sps[-1]+int(x)>maxs and k>4:
            maxs=max(maxs,sps[-1]+int(x))
            R = k
        sps.append(sps[-1]+int(x))
        k+=1
sps.pop(0)
#print(sps)
#print(maxs)
k=0
for x in sps[:R]:
    if x < mins1:
        mins1 = x
        L = k
    k+=1
k=0
for x in sps[L+1:R]:
    if x< mins2:
        mins2 = x
        M = k
    k+=1
print(mins1, mins2, maxs)
print(L, M, R)
#print(sp)
print(sum(sp[M+2:R+1])- sum(sp[L+1:M+2]))
print(sps[R]-sps[M],(sps[M]-sps[L]))

