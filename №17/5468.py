a = open('5468.txt').readlines()
c = [int(x) for x in a]
k = []
minNumber = 1000000000
for i in c:
    if i % 103 == 0:
        minNumber = min(minNumber, i)
for i in range(len(c) - 1):
    if ((c[i] + c[i+1]) % 2) == 0 and (abs(c[i] - c[i+1]) % minNumber) == 0:
        k.append([c[i], c[i+1]])
print(len(k), max([sum(x) for x in k]))