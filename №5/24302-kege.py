def pr(n):
    s = ''
    while n:
        s = s + str(n%3)
        n = n//3
    return s[::-1]
minn = float('inf')
for n in range(167, 1000):
    r = pr(n) #12200 [1, 2, 2, 0, 0]
    sm = sum([int(x) for x in r])#r.count('1')+r.count('2')*2
    if sm%9==0:
        r = r + '2'
    else:
        ost = pr(sm%9)
        r = r + ost
    r=int(r, 3)
    minn = min(minn, r)
print(minn)
