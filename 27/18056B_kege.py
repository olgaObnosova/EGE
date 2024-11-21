with open('27B_18056.txt') as f:
    x = f.readline()
    zv = [[float(x.replace(',', '.')) for x in line.split()] for line in f]
kl1 = [x for x in zv if x[0] > 0.2 and x[1] < 0]
kl2 = [x for x in zv if x[0] < 0.8 and (-1<x[1]<3)]
kl3 = [x for x in zv if x[0] > 0.2 and (2<x[1]<6)]
cnt1, mins = 0, float('inf')
for i in range(len(kl1)):
    s = 0
    for j in range(len(kl1)):
        x1, y1 = kl1[i]
        x2, y2 = kl1[j]
        s+=((x1-x2)**2 + (y1 - y2)**2)**0.5
    if s<mins:
        mins=s
        cnt1 = kl1[i]
cnt2, mins = 0, float('inf')
for i in range(len(kl2)):
    s = 0
    for j in range(len(kl2)):
        x1, y1 = kl2[i]
        x2, y2 = kl2[j]
        s+=((x1-x2)**2 + (y1 - y2)**2)**0.5
    if s<mins:
        mins=s
        cnt2 = kl2[i]
cnt3, mins = 0, float('inf')
for i in range(len(kl3)):
    s = 0
    for j in range(len(kl3)):
        x1, y1 = kl3[i]
        x2, y2 = kl3[j]
        s+=((x1-x2)**2 + (y1 - y2)**2)**0.5
    if s<mins:
        mins=s
        cnt3 = kl3[i]
sr1 = (cnt1[0]+cnt2[0]+cnt3[0])/3
sr2 = (cnt1[1]+cnt2[1]+cnt3[1])/3
print(sr1*100_000, sr2*100_000)
