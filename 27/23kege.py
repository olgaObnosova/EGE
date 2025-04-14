s=0
minr=float('inf')
with open('27-A_23.txt') as f:
    n=int(f.readline())
    for x in f:
        a, b = map(int, x.split())
        s+=max(a, b)
        if abs(a-b)%3!=0:
            minr = min(minr, abs(a-b))
if s%3==0:
    print(s-minr)
else:
    print(s)

