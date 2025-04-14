s = [int(x) for x in open('17-354.txt')]
sp = []
sp2 = []
minn = 0
minni = []
for j in s:
    minni.append(j)
minn = min(minni)
print(minn)
def l(o):
    if (s[o]**2 + s[o+1]**2) > minn**2:
        return 1
    else:
        return 0

def f(n):
    if abs(abs(s[n])%10 - abs(s[n+1])%10) == 1:
        return 1
    else:
        return 0

def g(k):
    if (s[k]%5 == 0 and s[k+1]%5 !=0) \
            or (s[k]%5 != 0 and s[k+1] %5 == 0):
        return 1
    else:
        return 0

for i in range(len(s) - 1):
    p1 = f(i)
    p2 = g(i)
    p3 = l(i)
    if (p1+p2+p3)==3:
        sp.append(s[i]+s[i+1])
        if (s[i]+s[i+1])>0:
            sp2.append(s[i]+s[i+1])
print(len(sp), min(sp2))