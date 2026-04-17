with open('9_5крылов') as f:
	sp=[[int(x) for x in line.split()] for line in f]
print(sp[:5])
k=0
for line in sp:
	maxx = max(line)
	s = sum(line)-maxx
	if maxx<s and len(set(line))==4:
		k+=1
print(k)