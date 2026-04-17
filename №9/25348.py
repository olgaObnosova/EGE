with open('25348') as f:
	sp = [[int(x) for x in line.split()] for line in f]
k = 0
for line in sp:
	pov = [x for x in line if line.count(x) == 3]
	nep = [x for x in line if line.count(x) == 1]
	if len(pov) == 3 and len(nep) == 4:
		maxc = max(line)
		if maxc not in pov:
			k+=1
print(k)