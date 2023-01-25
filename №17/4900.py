a = open("4900.txt").readlines()

c = [int(x) for x in a]
MAXELEM = max(c)
spisok = []
minNumber, maxNumber = 4000, -5000
for i in range(0, len(c) - 2):
    if c[i] + c[i+1] + c[i+2] < MAXELEM:
        spisok.append([c[i], c[i+1], c[i+2]])
        minNumber = min(c[i], c[i+1], c[i+2], minNumber)
        maxNumber = max(c[i], c[i+1], c[i+2], maxNumber)
print(len(spisok), minNumber + maxNumber)
