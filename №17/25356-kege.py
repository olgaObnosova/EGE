with open('17_25356.txt') as f:
	sp = [int(x) for x in f]
max_30 = 0
for x in sp:
	if x%100==30:
		max_30=max(max_30, x)
print(max_30)
#print(abs(-130)%100)
k=0
maxs=0
for i in range(len(sp)-2):
	p1 = len(str(abs(sp[i])))!=4 #1
	p2 = len(str(abs(sp[i+1])))!=4
	p3 = len(str(abs(sp[i+2])))!=4
	if p1+p2+p3==3:
		if sp[i]+sp[i+1]+sp[i+2]>max_30:
			k+=1
			maxs = max(maxs, sp[i]+sp[i+1]+sp[i+2])
print(k, maxs)