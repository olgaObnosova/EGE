max0=0
for x in range(1, 232):
	a = 64**678 + 55**123 - x
	k0=0
	while a:
		if a%25==0:
			k0+=1
		a=a//25
	max0 = max(max0, k0)
print(max0)