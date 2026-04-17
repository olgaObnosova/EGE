def centre(kl):
	mins = float('inf')
	for x1, y1 in kl:
		s = 0
		for x2, y2 in kl:
			s+=((x2-x1)**2+(y2-y1)**2)**0.5
		if s < mins:
			mins = s
			cnt = x1, y1
	return cnt
with open('27_B.txt') as f:
	sp = [[x for x in line.split()] for line in f]
print(sp[:2])
sp1 = [[float(x.replace(',', '.')) for x in line[:2]] for line in sp]
print(sp1[:2])
kl1 = [line for line in sp1 if line[1]>23]
kl2 = [line for line in sp1 if line[1]<23 and line[1]>16]
kl3 = [line for line in sp1 if line[1]<16]

print(len(sp1), len(kl1), len(kl2), len(kl3))
cnt1 = centre(kl1)
cnt2 = centre(kl2)
cnt3 = centre(kl3)
gig = []
print(cnt1)
print(cnt2)
print(cnt3)
for line in sp:
	hr = line[-1]
	if hr[0]=='Z' and hr[-2:]=='IV':
		gig.append(line)
print(len(gig))
minr = float('inf')
k1=k2=k3=0
for x1, y1, sv in gig:
	x1 = float(x1.replace(',','.'))
	y1 = float(y1.replace(',','.'))
	if [x1, y1] in kl1:
		k1+=1
	if [x1, y1] in kl2:
		k2+=1
	if [x1, y1] in kl3:
		k3+=1
	for x2, y2, sv2 in gig:
		x2 = float(x2.replace(',','.'))
		y2 = float(y2.replace(',','.'))
		if [x1, y1]!=[x2, y2] and (([x1, y1] in kl1) + ([x2, y2] in kl1) ==2 \
			or ([x1, y1] in kl2) + ([x2, y2] in kl2) == 2\
			or ([x1, y1] in kl3) + ([x2, y2] in kl3) == 2):
			r = ((x2-x1)**2+(y2-y1)**2)**0.5
			if r < minr:
				minr = r
print(minr*10_000)
print(k1, k2, k3)
x1, y1 = cnt1
x2, y2 = cnt3
rotv = ((x2-x1)**2+(y2-y1)**2)**0.5
print(rotv*10_000)