a = open("5072.txt").readlines()
c = [int(x) for x in a]
k = []

def sumNumber(n):
    n = int(n)
    nach = 0
    for i in str(n):
        nach += int(i)
    return nach
maxSum = 0

srarfm = sum(c) / len(c)

for i in range(len(c) - 1):
    if (c[i] + c[i+1]) > srarfm and sumNumber(str(c[i]) + str(c[i+1])) ** 0.5 == int(sumNumber(str(c[i]) + str(c[i+1])) ** 0.5):
        maxSum = max(maxSum, sumNumber(str(c[i]) + str(c[i+1])))
        k.append([c[i], c[i+1]])
print(len(k), maxSum)
