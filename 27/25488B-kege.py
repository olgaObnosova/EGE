def ctnter(kl):
	minn = float('inf')
	for x1, y1 in kl:
		s=0
		for x2, y2 in kl:
			r = ((x2-x1)**2+(y2-y1)**2)**0.5
			s+=r
		if s<minn:
			minn=s
			cnt = x1, y1
	return cnt
with open('27B_25448.txt') as f:
	sp=[[float(x.replace(',', '.')) for x in line.split()] for line in f]
kl1 = [line for line in sp if 23<line[0]<33]
kl2 = [line for line in sp if 9<line[0]<21 and line[1]<16]
kl3 = [line for line in sp if 9<line[0]<23 and line[1]>16]
print(len(sp), len(kl1),len(kl2), len(kl3))
cnt1 = ctnter(kl1)
cnt2 = ctnter(kl2)
cnt3 = ctnter(kl3) #!
x1, y1 = cnt3
s3=0
for i in range(len(kl3)):
	x2, y2 = kl3[i]
	r = ((x2-x1)**2+(y2-y1)**2)**0.5
	s3 +=r
q1 = s3/(len(kl3)-1)
x1, y1 = cnt1
s1=0
for i in range(len(kl1)):
	x2, y2 = kl1[i]
	r = ((x2-x1)**2+(y2-y1)**2)**0.5
	s1 +=r
q2 = s1/(len(kl1)-1)
print(q1*10_000, q2*10_000)