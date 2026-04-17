with open('27A_25444.txt') as f:
	sp = [[float(x.replace(',','.')) for x in line.split()] for line in f]
	kl1 = [line for line in sp if line[1] < 8]
	kl2 = [line for line in sp if line[1] > 8 and line[0] < 15]
print(len(kl1), len(kl2), len(sp))
minx1 = float('inf')
minx2 = float('inf')
minx3 = float('inf')
center1 = 4.0212698206, 0.9530632976
center2 = 6.9951620444, 9.0097921893
minx = float('inf')
for i in range(len(kl1)):
	s = 0
	x1, y1 = kl1[i]
	for j in range(len(kl1)):
		x2,y2 = kl1[j]
		r = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
		s = s + r
	if s < minx1:
		minx1 = s
		center1 = x1, y1
for i in range(len(kl2)):
	s = 0
	x1, y1 = kl2[i]
	for j in range(len(kl2)):
		x2,y2 = kl2[j]
		r = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
		s = s + r
	if s < minx2:
		minx2 = s
		center2 = x1, y1
# for i in range(len(kl2)):
#     x1, y1 = kl2[i]
#     r = ((center1[0] - x1)**2 + (center1[1] - y1)**2)**0.5
#     minx = min(r, minx)
# print(minx)
# for i in range(len(kl1)):
#     x1, y1 = kl1[i]
#     r = ((center2[0] - x1)**2 + (center2[1] - y1)**2)**0.5
#     minx = min(r, minx)
# print(minx)