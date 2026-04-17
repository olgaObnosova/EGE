def cnt(kl):
	minn=float('inf')
	for i in range(len(kl)):
		s=0
		x1, y1 = kl[i]
		for j in range(len(kl)):
			x2, y2 = kl[j]
			r = ((x2-x1)**2+(y2-y1)**2)**0.5
			s+=r
		if s<minn:
			minn=s
			centre = kl[i]
	return centre

with open('23766A') as f:
	sp = [[float(x.replace(',','.')) for x in line.split()] for line in f]
kl1 = [line for line in sp if line[1]>10]
kl2 = [line for line in sp if line[1]<10]
centre1 = cnt(kl1)
centre2 = cnt(kl2)
print(centre1)
print(centre2)
px = min(centre1[0], centre2[0])
py = min(centre1[1], centre2[1])
print(int(px*10_000), int(py*10_000))