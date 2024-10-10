file = open("27A_yak1.txt")
stars = [[float(j) for j in i.split()] for i in file]
stars.sort(key=lambda x: x[-1])
centroid1=stars[-2]
centroid2=stars[-1]
klaster1 = [star for star in stars if ((star[0]-centroid1[0])**2+\
            (star[1]-centroid1[1])**2+(star[2]-centroid1[2])**2)**0.5< \
            ((star[0] - centroid2[0])**2 + \
            (star[1] - centroid2[1])**2 + \
            (star[2] - centroid2[2])**2)**0.5]
klaster2 = [star for star in stars if ((star[0]-centroid1[0])**2+\
            (star[1]-centroid1[1])**2+(star[2]-centroid1[2])**2)**0.5> \
            ((star[0] - centroid2[0])**2 + \
            (star[1] - centroid2[1])**2 + \
            (star[2] - centroid2[2])**2)**0.5]
print(len(klaster2))
print(len(klaster1))
print(len(stars))