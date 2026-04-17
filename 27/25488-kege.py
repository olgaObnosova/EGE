with open('27A_25448.txt') as f:
	sp= [[float(x.replace(',','.')) for x in line.split()] for line in f]
kl1 = [line for line in sp if line[1]<10]
kl2 = [line for line in sp if line[1]>10 and line[0]>0 and line[0]<10]
print(len(sp), len(kl1), len(kl2))
minn = float('inf')
for x1, y1 in kl1:
	s = 0
	for x2, y2 in kl1:
		r = ((x1-x2)**2+(y1-y2)**2)**0.5
		s+=r
	if s<minn:
		minn=s
		cnt1 = x1, y1
minn2 = float('inf')
for x1, y1 in kl2:
	s = 0
	for x2, y2 in kl2:
		r = ((x1-x2)**2+(y1-y2)**2)**0.5
		s+=r
	if s<minn2:
		minn=s
		cnt2 = x1, y1
print(cnt1)
print(cnt2)
px=abs(cnt1[0]-cnt2[0])
py=abs(cnt1[1]-cnt2[1])
print(px*10_000)
print(py*10_000)