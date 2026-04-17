def dl(n):
	s = []
	for i in range(2, int(n**0.5)+1):
		if n%i==0:
			if pr(i) and str(i).count('5')==1:
				s.append(i)
			if pr(n//i) and str(n//i).count('5')==1:
				s.append(n//i)
	return s
def pr(n):
	for i in range(2, int(n**0.5)+1):
		if n%i==0:
			return False
	return True
for i in range(1_324_728, 10**10):
	d = dl(i)
	if len(d)>0: # [2, 5, 10, 10]
		for x in d:
			for y in d:
				if x * y == i:
					print(i, max(x, y))
					break