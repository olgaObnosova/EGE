with open('17_23276.txt') as f:
	sp=[int(x) for x in f]
max25=0
for x in sp:
	if x%100==25:
		max25 = max(max25, x)
print(max25)
#print(abs(-125)%100)
k=0
maxs = 0
for i in range(len(sp)-2):
	p1 = len(str(abs(sp[i])))==4 #T
	p2 = len(str(abs(sp[i+1])))==4#T
	p3 = len(str(abs(sp[i+2])))==4#F
	if p1+p2+p3<=2:
		if sp[i]+sp[i+1]+sp[i+2]<=max25:
			k+=1
			maxs = max(maxs, sp[i]+sp[i+1]+sp[i+2])
print(k, maxs)