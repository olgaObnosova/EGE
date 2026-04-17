with open('27B_25448.txt') as f:
	sp=[[float(x.replace(',', '.')) for x in line.split()] for line in f]
kl1 = [line for line in sp if 23<line[0] < 33]
kl2 = [line for line in sp if line[1] < 16 and 9 < line[0] < 19]
kl3 = [line for line in sp if line[1] > 15 and 12 < line[0] < 23]
print(len(sp), len(kl1), len(kl2), len(kl3)) #3
#print(kl1)
mins=10**10
for x1, y1 in kl1:
	s = 0
	for x2, y2 in kl1:
		r = ((x1-x2)**2+(y1-y2)**2)**0.5
		s+=r
	if s<mins:
		mins=s
		centre1 = x1, y1
mins2=10**10
for x1, y1 in kl2:
	s = 0
	for x2, y2 in kl2:
		r = ((x1-x2)**2+(y1-y2)**2)**0.5
		s+=r
	if s<mins2:
		mins2=s
		centre2 = x1, y1
mins3=10**10
for x1, y1 in kl3:
	s = 0
	for x2, y2 in kl3:
		r = ((x1-x2)**2+(y1-y2)**2)**0.5
		s+=r
	if s<mins3:
		mins3=s
		centre3 = x1, y1
print(centre1, centre2, centre3)
x1, y1 = centre3
sr=0
for x2, y2 in kl3:
	sr+=((x1-x2)**2+(y1-y2)**2)**0.5
q1 = sr/87
x1, y1 = centre1
sr2=0
for x2, y2 in kl1:
	sr2+=((x1-x2)**2+(y1-y2)**2)**0.5
q2 = sr2/398
print(q2*10_000)