with open('24_2508.txt') as f:
    maxx=0
    kc=0
    for x in f:
        kc+=x.count('C')
        k=x.count('Q')
        if k>=maxx:
            maxx=k
            otv = x
import string as s
alf=s.ascii_uppercase
print(alf)
otv = otv.strip()
sp=[0]*26
buk = set(otv)
for x in buk:
    ind = alf.find(x)
    sp[ind]=otv.count(x)
print(sp)
print(sp.index(22))
print(alf[2]) #C
print(kc)