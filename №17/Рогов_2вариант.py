def dl(n):
	s=set()# 1 2 3 4 5 6 7 8 9 10
	for i in range(1, int(n**0.5)+1):
		if n%i==0: #100%2==0
			s.add(i) # 2
			s.add(n//i) #100//2
	return s
#print(dl(100))
with open('17.txt') as f:
	sp=[int(x) for x in f]
maxx=0
for x in sp:
	kd = len(dl(x))
	if kd>maxx:
		maxx=kd
		ch = x
print(ch, len(dl(ch)))
d = dl(ch) #820
k=maxob=0
for i in range(len(sp)-1): #1 2 3 4
	d1 = dl(sp[i]) # делители 1 числа в паре
	d2 = dl(sp[i+1])# делители 2 числа в паре
	p1 = d&d1
	p2 = d&d2
	if len(p1)>=3 and len(p2)>=3:
		k+=1
		ob = d1&d2
		maxob = max(maxob, len(ob))
print(k, maxob)