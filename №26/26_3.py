with open('pr') as f:
    n, m, k= map(int, f.readline().split())
    sp=[[int(x) for x in line.split()] for line in f]
print(n, m, k)
sp.sort(key=lambda x: x[1])
otv=[[0,0]]*k
posl=[0]*k
for x in sp:
    gor, vert=x
    if abs(posl[vert]-vert)>otv[gor][0]:
        otv[gor][0]=abs(posl[gor]-gor)
        otv[gor][1]=gor
    posl[gor]=gor
print(max(otv))