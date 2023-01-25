f = open('/home/student/PycharmProjects/666.txt')
cnt =0
cnt1 = 0
a =[]
for s in f:
    a.append(int(s))
sr = sum(a)/len(a)
for i in range(len(a)-2):
    if (a[i] < sr) or (a[i+1]<sr) or (a[i+2]<sr):
        if '9' in str(a[i]) and '9' in str(a[i+1]) and '9' in str(a[i+2]):
            cnt+=1
            cnt1 = max(cnt1,a[i]+a[i+1]+a[i+2])
print(cnt)
print(cnt1)





