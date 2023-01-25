f = open('/home/student/PycharmProjects/666.txt')
cnt =0
cnt1 = 0
a =[]
for s in f:
    a.append(int(s))
sr = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i] > sr) or (a[i+1]>sr):
        if (str(a[i])[-1] == '3') or (str(a[i+1])[-1] == '3'):
            cnt += 1
            cnt1 = max(cnt1,a[i]+a[i+1])
print(cnt)
print(cnt1)





