import ipadress as ip
for i in range(32):
	comb = ip.ip_network(f'132.118.34.161/{i}', 0)
	k=0
	for x in comb:
		ad = bin(int(x))[2:]
		k1 = ad.count('1')
		if k1==13:
			k+=1
	if k==35:
		print(i)