#https://kompege.ru/variant?kim=25003662
f=open("27-A_25003662.txt")
b=0
d=[]
m=0
for i in range(int(f.readline())):
    a=list(map(int,f.readline().split()))
    d.append(max(a)-min(a))
    b+=max(a)
    m+=min(a)
d.sort()
print(d)
c=b
x=m
for i in range(len(d)):
    if ((b-d[i])%5!=0 and (m+d[i])%3!=0):
        print(b - d[i])
        break
    if ((c-d[i])%5!=0 and (x+d[i])%3!=0):
         print(c-d[i])
         break
    else:
        c-=d[i]
        x+=d[i]
