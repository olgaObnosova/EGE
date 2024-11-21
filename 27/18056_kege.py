import math
with open('27A_18056.txt') as file:
    stars = [[float(x.replace(',','.')) for x in line.split()] for line in file]
kl1=[st for st in stars if st[1]>-0.5 and st[0]<1]
kl2=[st for st in stars if st[1]<-1 and st[0]>0.5]
centr1, mins = 0, float('inf')
for i in range(len(kl1)):
    s=0
    for j in range(len(kl1)):
        if i==j:
            continue
        x1, y1, =kl1[i]
        x2, y2, = kl1[j]
        s+=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if s<mins:
        mins=s
        centr1 = kl1[i]
centr2, mins = 0, float('inf')
for i in range(len(kl2)):
    s = 0
    for j in range(len(kl2)):
        if i == j:
            continue
        x1, y1, = kl2[i]
        x2, y2, = kl2[j]
        s += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if s < mins:
        mins = s
        centr2 = kl2[i]

srx=(centr1[0]+centr2[0])/2
sry=(centr1[1]+centr2[1])/2
print(srx*100_000, sry*100_000)

