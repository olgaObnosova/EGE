print([bin(int(x))[2:] for x in '192.168.32.160'.split('.')])
print([bin(int(x))[2:] for x in '255.255.255.240'.split('.')])
import itertools as t
l=list(t.product('01', repeat=4))
k=8
cnt=0
for x in l:
    if (k+x.count('1'))%2==0:
        cnt+=1
print(cnt)