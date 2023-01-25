f = open("/home/student/PycharmProjects/Vex1cK's/17.txt")
a = []
cnt = 0
cnt1 = 0
for s in f:
    a.append(int(s))
for i in range(len(a)-1):
    if ( a[i]%7==0 or a[i+1]%7==0       ) and (a[i]+a[i+1])%5==0:
        cnt+=1
        cnt1 = max(cnt1,a[i]+a[i+1])
print(cnt,cnt1)


