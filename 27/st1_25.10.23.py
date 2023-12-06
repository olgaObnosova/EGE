with open('27-st_25.10.23B.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
maxx1=maxx2=maxs=0
for i in range(n-3*k):
    maxx1=max(maxx1, sp[i])
    maxx2= max(maxx2, sp[i+1])
    maxs= max(maxs,maxx1+sp[i+3*k]+maxx2)
print(maxs)