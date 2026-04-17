with open('9. 27-A.txt') as s:

	sp = [[float(x.replace(',', '.')) for x in line.split()]for line in s]
kl1 = [x for x in sp if x[0]<0 and x[1]< 0]
kl2 = [x for x in sp if x[0]>0 and x[1]> 0]
print(len(sp), len(kl1)+len(kl2))