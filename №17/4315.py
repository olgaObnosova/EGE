a = [int(x) for x in open('17.txt')]
ans = []
for i in range(len(a)):
    if (int(str(a[i])[-2])) <= 4 and 3 <= (int(str(a[i])[-3])) <= 7 :
        ans.append(a[i])
print(len(ans), min(ans))
