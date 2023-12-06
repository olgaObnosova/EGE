import time
start = time.time()
with open('pr') as f:
    n, k = map(int, f.readline().split())
    sp=[int(x) for x in f]
summy = [0]*n
for i in range(n):
    summy[i]=summy[i-1]+sp[i]
print(sp)
print(summy)
maxx=-float('inf')
minn=float('inf')
for i in range(k+1, n):
    minn=min(minn, summy[i-(k+1)])
    maxx=max(maxx,summy[i]-minn)
print(maxx)
end = time.time() - start
print(end)
