file = open("17_3v.txt")
pairs = []
absolute = 0
maxx = 0
numbers = [int(i) for i in file]
for i in numbers:
    if abs(i) < 100:
        absolute += 1
for i in range(len(numbers)-1):
    #print(numbers[i],i)
    if (numbers[i+1] + numbers[i]) / 2 > absolute:
        maxx = max(maxx, numbers[i+1] + numbers[i])
        pairs.append([numbers[i+1], numbers[i]])
print(len(pairs), maxx)
