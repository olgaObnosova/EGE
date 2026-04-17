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
def maxr(kl, cent):
	maxx=-float('inf')
	x1, y1 = cent
	for i in range(len(kl)):
		x2, y2 = kl[i]
		r = ((x2-x1)**2+(y2-y1)**2)**0.5
		if r>maxx:
			maxx=r
	return maxx
with open('27_B_23766.txt') as f:
	sp = [[float(x.replace(',','.')) for x in line.split()] for line in f]
kl1 = [line for line in sp if line[0]>19 and line[0]<29]
kl2 = [line for line in sp if line[1]>20 and line[1]<30 and line[0]>11 and line[0]<18]
kl3 = [line for line in sp if line[1]>6 and line[1]<18 and line[0]>7 and line[0]<15]
print(len(sp), len(kl1), len(kl2), len(kl3))
centre1 = cnt(kl1)
centre2 = cnt(kl2)
centre3 = cnt(kl3)
x1, y1= centre1
x2, y2 = centre3
q1 = ((x2-x1)**2+(y2-y1)**2)**0.5
print(int(q1*10_000))
r1 = maxr(kl1, centre1)
r2 = maxr(kl2, centre2)
r3 = maxr(kl3, centre3)
q2 = max(r1, r2, r3)
print(int(q2*10_000))