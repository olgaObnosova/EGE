with open('6798b.txt') as f:
    n, k = map(int, f.readline().split())
    sp=[int(x) for x in f]
max1=max2=maxs=0
for i in range(2*k,n):
    max1=max(max1,sp[i-2*k])
    max2=max(max1*sp[i-k],max2) #max2=max(max2, max1+sp[i-k])
    maxs=max(maxs,max2*sp[i])
print(maxs%(10**6+1))