with open('primer.txt') as f:
    n=int(f.readline())
    k=int(f.readline())
    sp=[int(x) for x in f]
max1=max2=maxs=0
for i in range(2*k,n):
    max1=max(max1,sp[i-2*k])
    max2=max(max2,sp[i-k]) #max2=max(max2, max1+sp[i-k])
    maxs=max(maxs,max2+sp[i])
print(maxs)