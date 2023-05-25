with open('primer.txt') as f:
    n=f.readline()
    count=0
    pr=1
    M=20
    sp=[0]*20
    for x in f:
        pr*=int(x)
        if pr%M!=0:
            count+=1
        count+=sp[not(pr%2)*pr//2]
        sp[not(pr%2)*pr//2]+=1
        print(sp)

print(count)

