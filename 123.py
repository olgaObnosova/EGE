import itertools as t
n=int(input())
sp=[]
s = list(t.product('23456789', repeat=3))
#print(s[0])
while len(sp)<n:
    pr=1
    #print(sp)
    for y in s:
        for x in y:
            pr*=int(x)
    if len(str(pr))==3:
        sp.append(pr)
print(*sp)

