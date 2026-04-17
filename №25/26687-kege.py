def delit(n):
	sp = []
	for i in range(2,(int(n**0.5))+1):
		if n%i==0:
			sp.append(i)
			sp.append(n//i)
	return sorted(sp)
def prost(n):
	for i in range(2, int(n**0.5)+1):
		if n%i==0:
			return False
	return True
for i in range(89427151, 894271510):
	d = delit(i)
	#print(d)
	pr =[]
	for x in d:
		if prost(x):
			pr.append(x)
	#print(pr)

	if len(pr)>0:
		mind = min(pr)
		pr.remove(mind) # [ 5, 17, 1193] [3, 7] 2
		#print(mind, pr)
		if mind**2 not in d:
			par=[]
			for cl in pr:
				if cl**2 in d:
					par.append(cl) #[3, 7]
			#print(par)
			if len(par)==2:
				pr.remove(par[0])
				pr.remove(par[1]) #[2, 566666, 566667]
				proiz = 1
				#print(pr)
				#break
				for t in pr:
					proiz*=t
				proiz=proiz*mind*par[0]**2*par[1]**2
				if i==proiz and len(pr)==3:
					print(i, max(max(pr), max(par)))