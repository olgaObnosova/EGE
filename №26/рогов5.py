with open('26.txt') as f:
	k = int(f.readline())
	n = int(f.readline())
	sp = [[int(x) for x in line.split()] for line in f]
okno = [0] * k
cnt = 0
for line in sp:
	#print(okno)
	st, end = line
	for i in range(k):
		if st >= okno[i]:
			okno[i] = end
			cnt += 1
			r = i
			break
		else:
			minokno=min(okno)
			if minokno<=end:
				ind = okno.index(minokno)
				okno[ind]=end
				cnt += 1
				r = i
				break

print(cnt, r+1)