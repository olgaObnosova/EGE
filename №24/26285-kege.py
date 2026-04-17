with open('24_26285.txt') as f:
	sp = f.readline()
sp = sp.replace('A', '%')
sp = sp.replace('E', '%')
sp = sp.replace('B', '@')
sp = sp.replace('C', '@')
sp = sp.replace('D', '@')
sp = sp.replace('F', '@')
maxx = 0
k = 0
i = 0
while i < len(sp) - 5:  # i=0
	z = sp[i:i + 5]
	print(z, i, k, maxx)
	while z.count('@') > z.count('%') and i < len(sp) - 5:
		z = sp[i:i + 5]
		i = i + 5
		k += 1
		# print(k, i)
		maxx = max(maxx, k)
	else:
		i = i - k * 5 + 1
		k = 0
print(maxx)