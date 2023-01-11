f=open("input")

a=sorted(list(map(int,f.readline().split())))
d=[]
sum=0
while a!=[]:
    d.append(max(a)-a[0])
    d.append(max(a)-a[1])
    sum+=a[1]+a[0]
    a = sorted(list(map(int, f.readline().split())))
d=sorted(d)
sum1=sum
i=0
while True:
    if ((sum1+d[i]) % 3 == 0 or (sum1+d[i]) % 17 == 0) and not((sum1+d[i]) % 3 == 0 and (sum1+d[i]) % 17 == 0):
        print(sum1+d[i])
    if (sum%3==0 or sum%17==0) and not(sum%3==0 and sum%17==0):
        print(sum)
    sum+=d[i]
    i+=1
