def raspred(dat): #автоматическое распределение
    crs=[]
    while len(dat) > 0:
        crs += [[dat.pop()]]
        for p0 in crs[-1]:
            cr = [p for p in dat if d(p0, p) <= 5.5]
            for p in cr: dat.remove(p)
            crs[-1] += cr
    return crs
def d(x1, y1, x2, y2):
    r = (x2-x1)**2+(y2-y1)**2
    return r**0.5
def centr(kl):
    minn=float('inf')
    for i in range(len(kl)):
        x1, y1, = kl[i]
        s=0
        for j in range(len(kl)):
            x2, y2, = kl[j]
            s+=d(x1, y1, x2, y2)
        if s<minn:
            centrkl= kl[i]
            minn=min(minn, s)
    return centrkl


with open('27_st_А.txt') as f:
    sp=[[float(x) for x in line.replace(',','.').split()] for line in f]
kl1=[x for x in sp if x[1]<-7]
kl2=[x for x in sp if x[1]>-7 and x[1]<x[0]-11]
kl3=[x for x in sp if x[1]>x[0]-11]
ckl1=centr(kl1)
ckl2=centr(kl2)
ckl3=centr(kl3)
print((ckl1[0]+ckl2[0]+ckl3[0])/3*10_000)
print((ckl1[1]+ckl2[1]+ckl3[1])/3*10_000)

