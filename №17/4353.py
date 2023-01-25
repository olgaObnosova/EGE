f = open("/home/student/PycharmProjects/Vex1cK's/4353.txt")
a = []
mk = 0
k = 0
for s in f:
    a.append(int(s))
for i in range(len(a)-1):
    if  str(a[i])[-1] == "5":
        if str(a[i+1])[-1] == "5":
            k+=1
            mk = max(mk,a[i]+a[i+1])
print(k,mk)


