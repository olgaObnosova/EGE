a = [int(x) for x in open('17.txt')]
ans = []
minnum = 1000000
j = sum(a)/ len(a)
for i in range(len(a) -1):
    if (a[i] % 7 == 0 and a[i] % 3 != 0 and a[i] % 11 != 0  and a[i] % 13 != 0 and (a[i]< j or a[i+1]<j)) or  (a[i + 1] % 7 == 0 and a[i + 1] % 3 != 0 and a[i + 1] % 11 != 0 and a[i + 1] % 13 != 0 and (a[i]< j or a[i+1]<j)):
        ans.append([a[i], a[i+1]])
        b = a[i] + a[i + 1]
for i in ans:
    minnum = min(minnum, sum(i))
print(len(ans), minnum)
