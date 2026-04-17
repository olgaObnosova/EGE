with open('24_23381.txt') as f:
	f=f.readline()
for x in '02468':
	f=f.replace(x, '*')
f=f.split('*')
maxk=0
for x in f:
	k=1
	if x.isalpha():
		for i in range(len(x)-1):
			if x[i]==x[i+1]:
				k+=1
				if len(x)==k:
					maxk=max(maxk, k)
			else:
				break
print(maxk+2)