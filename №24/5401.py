from fnmatch import fnmatch
k = 0
j = 0
c = []
a = open("5401.txt").readline()
maxLen = 0
for i in range(0, len(a)):
    if a[i] == "A":
        while k < 4:
            try:
                if a[i + j] == "A":
                    k += 1
            except:
                break
            j += 1
        if k == 4:
            c.append(a[i:i+j])
    j = 0
    k = 0
otvet = []
for i in c:
    m = []
    for k in i.split("A"):
        m.append(k)
    for j in m:
        if i.count(j) == 3 and i.split("A")[1] == i.split("A")[2] == i.split("A")[3]:
            otvet.append(i)
for i in otvet:
    maxLen = max(maxLen, len(i))
print(maxLen)