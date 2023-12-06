with open('27-6799b.txt') as f:
    n, k = map(int, f.readline().split())
    sp=[0]*k
    sh=otv=i=0
    for x in f:
        x=int(x)
        if x>=k:
            otv+=i
            sh+=1
        else:
            otv+=sum(sp[k-x:])+sh
            sp[x]+=1
        i+=1
print(otv)