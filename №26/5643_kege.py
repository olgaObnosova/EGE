with open('5643.txt') as f:
    sp=[]
    zam =[]
    m,n = map(int, f.readline().split())
    for line in f:
        sp.append(int(line.split()[0]))
        if len(line.split())==2:
            zam.append(int(line.split()[1]))
sp.sort()
print(sp[:20])
otv = [242]
print(242 in zam)
for i in range(2, len(sp)):
    if otv[-1] % 2 != sp[i] % 2 and \
            sp[i] - otv[-1] >= 9 and  sp[i] in zam:
        otv.append((sp[i]))
print(otv)
print(len(otv))




