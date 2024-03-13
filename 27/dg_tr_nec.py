with open('27_A_11.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
print(k)
max1=max2n=max2c=maxs=0
for i in range(2*k,n):
    max1=max(max1,sp[i-2*k])
    if (max1+sp[i-k])%2==0:
        max2c=max(max1+sp[i-k], max2c)
    else:
        max2n = max(max1+sp[i - k], max2n)
    #max2=max(max2, max1+sp[i-k])
    if sp[i]%2==0:
        maxs=max(max2n+sp[i], maxs)
    else:
        maxs = max(max2c+ sp[i], maxs)

print(maxs)