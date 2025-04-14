with open('26var03.txt') as f:
    n, m, k = map(int, f.readline().split())
    sp = [[int(x) for x in line.split()] for line in f]
sp.sort(key = lambda  x: (x[1],x[0]))
#print(sp[:10])
spdl=[0]*(k+1)
spposl=[0]*(k+1)
sptek=[0]*(k+1)
for x in sp:
    gor, vert = x
    if abs(sptek[vert]-gor) > spdl[vert]:
        spdl[vert] = abs(sptek[vert] - gor)
        spposl[vert] = gor
    sptek[vert] = gor
maxx= max(spdl)
vsemax=[]
for x in range(len(spdl)):
    if spdl[x]==maxx:
        vsemax.append((spposl[x], x))
vsemax.sort()
print(maxx)
print(vsemax)
print(vsemax[0][0]-1, vsemax[0][1])