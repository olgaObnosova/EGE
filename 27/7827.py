with open('27B_7827.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
mxc=mxn=mxs=0
for i in range(k, len(sp)):
    if sp[i-k]%2==0:
        mxc = max(mxc, sp[i-k])
    else:
        mxn = max(mxn, sp[i - k])
    if sp[i] % 2 == 0:
        mxs = max(mxs, sp[i]+mxn)
    else:
        mxs = max(mxs, sp[i]+mxc)
print(mxs)

