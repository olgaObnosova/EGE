f = open('/home/student/PycharmProjects/123.txt')
s=f.readline()
a=[]
ch=''
for i in s:
    if (i == '1' or i == '3' or i == '5' or i == '7' or i == '9') and int(i)%2!=0:
        ch+=i
        a.append(int(ch))
    else:
        ch=''
print(max(a))
