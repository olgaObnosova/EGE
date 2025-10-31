n, k = map(int, input().split())
sp = [int(x) for x in input().split()]
for i in range(n-k+1):
    sm = sum(sp[i:i+k])
    if sm%k==0:
        print(sm//k, end = ' ')
    else:
        print(f'{sm}/{k}', end=' ')