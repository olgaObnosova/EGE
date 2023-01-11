f=open("4844.txt")
a=list(map(int,f.readline().split()))
d1=list()
d2=list()

while a!="":
    try:
        a=list(map(int,f.readline().split()))
        if a[0]>=4854:
            d1.append(a[1])
        else:
            d2.append(a[1])

    except IndexError:
        break
d1=sorted(d1)
d2=sorted(d2)
i=0
final=10000000
count=0
time=0

while final>0:

    if i<len(d2):
        if final-d1[i]>=0:
            time += d1[i]
            final -= d1[i]
            count+=1
        else:
            break
        if final - d2[i] >=0:
            final -=d2[i]
            count+=1
        else:
            count-=1
            final += d1[i]
            time = time - d1[i]
            i+=1
            if final - d2[i]>=0:
                count+=1
            break
    else:
        break
    i+=1

print(count)
print(time)
print(final)





