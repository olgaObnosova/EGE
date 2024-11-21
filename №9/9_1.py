def ft(n):
    s=0
    for x in str(n):
        s+=int(x)
    return s
sp=[]
with open('9_1.txt') as f:
    k=0
    for x in f:
        k+=1
        x=[int(y) for y in x.split()]
        if x[0]<=x[1]<=x[2]<=x[3]<=x[4] and len(set(x))!=len(x):
            for y in x:
                if x.count(y)>1 and ft(y)%2==0:
                    sp.append(k)
                    break
print(sp)



