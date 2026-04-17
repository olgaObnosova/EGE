with open('26_23570.txt') as f:
	n, k = map(int, f.readline().split())
	sad=[]
	ybor=[]
	for i in range(n):
		sad.append(int(f.readline()))
	for i in range(k):
		a, b = map(int, f.readline().split())
		ybor.append((a, b)) # мощ цена
sad.sort()
ybor.sort(key = lambda x:(x[1], -x[0]))
sm=maxm=0
#print(sad)
#print(ybor)
for x in sad:
	for m, s in ybor:
		if m>=x:
			sm+=s
			maxm = max(maxm, m)
			break
print(sm, maxm)