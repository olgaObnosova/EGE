from math import sqrt

file = open("27_A_17882.txt")
stars = [[float(j) for j in i.split()] for i in file]
klaster1 = [star for star in stars if star[1] < 3]
klaster2 = [star for star in stars if star[1] > 3]

centroid1, S1 = None, float('inf')
for i in range(len(klaster1)):
    S = 0
    for j in range(len(klaster1)):
        if i == j:
            continue
        x1,y1 = klaster1[i]
        x2, y2 = klaster1[j]
        S += sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)
    if S < S1:
        centroid1 = klaster1[i]
        S1 = S

centroid2, S2 = None, float('inf')
for i in range(len(klaster2)):
    S = 0
    for j in range(len(klaster2)):
        if i == j:
            continue
        x1,y1 = klaster2[i]
        x2, y2 = klaster2[j]
        S += sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)
    if S < S2:
        centroid2 = klaster2[i]
        S2 = S
cr_ar_x = (centroid1[0] + centroid2[0]) / 2
cr_ar_y = (centroid1[1] + centroid2[1]) / 2
print(cr_ar_x * 10_000, cr_ar_y * 10_000)