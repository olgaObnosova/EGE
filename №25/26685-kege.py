def delit(n):
	sp=[]
	for i in range(2,(int(n**0.5)+1)):
		if n%i==0:
			sp.append(i)
			sp.append(n//i)
	return sorted(sp)
def prost(n):
	sp=[]
	for i in range(2,(int(n**0.5)+1)):
		if n%i==0:
			return False
	return True
def prois(lst):
	p=1
	for x in lst:
		p*=x
	return p

for i in range(2722734,2722734+1):
	sp=[]
	d=delit(i)
	print(d)
	for x in d:
		if prost(x)==True:
			sp.append(x)
	print(sp)
	for b in sp: #  2, 3, 7
		print(b)
		for z in range(5,15):
			q = b**z
			if q in d:
				print(q, z)
				print(453789/7/7/7/7/7)
				if prois(sp) * q//b == i:
					print(i, b)
					break