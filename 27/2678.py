f=open("input.txt")
a=[]
c=0
m=f.readline()
for i in range(4):
    j=int(f.readline())
    for x in a:
        if (x*j)%13==0 and (x+j)%2==1:
            c+=1
    a.append(j)

for i in f:
    j=int(i)
    for x in a:
        if (x*j)%13==0 and (x+j)%2==1:
            c+=1
    a.pop(0)
    a.append(j)
print(c)


