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
with open('27_A_28766.txt') as f:
	sp = [[x for x in line.split()] for line in f]
print(sp[:2])
sp1 = [[float(x.replace(',', '.')) for x in line[:2]] for line in sp]
print(sp1[:2])
kl1 = [line for line in sp1 if line[1]>10]
kl2 = [line for line in sp1 if line[1]<10]
cnt1 = centre(kl1)
cnt2 = centre(kl2)
print(cnt1, cnt2)
print(len(kl1), len(kl2))