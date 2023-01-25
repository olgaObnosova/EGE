f = open('/home/student/PycharmProjects/666.txt')
cnt =0
cnt1 = 0
for s in f:
    a = int(s)
    if (hex(a))[-1] == 'b':
        if (a%7)==0 and (a%6)!=0 and (a%13)!=0 and (a%19)!=0:
            cnt += a
            cnt1 += 1
print(cnt)
print(cnt1)


