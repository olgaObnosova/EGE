with open('27A_дж8.txt') as f:
    k5=k7=cnt=otv=0
    n=f.readline()
    for x in f:
        x=int(x)
        if x%5==0:
            k5+=1
        if x%7==0:
            k7+=1
        if k5==k7:
            cnt+=1
        otv+=cnt
print(otv)