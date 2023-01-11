# 2669
f = open('B2669.txt')
a = []
min1=99999999
min2=99999999
m = int(f.readline())
for i in range(6):
    a.append(int(f.readline()))
# print(a)
for line in f:
    line=int(line)
    if a[0]<min1 and a[0]%2!=0:
        min1=a[0]
    if line<min2 and line%2!=0:
        min2=line
    #a.pop(0)
    #a.append(line)
    for i in range(5):
        a[i] = a[i + 1]
    a[5] = line
    # print(a)

print(min1*min2)
