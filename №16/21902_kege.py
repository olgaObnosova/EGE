import sys
sys.setrecursionlimit(10000)
def F(n):
    if n < 20:
        return n
    return (n-6)*F(n-7)
#print(F(1000))
#print(F(47872)-290*F(47865)//F(47858))
sp=[0]*47880
for i in range(47880):
    if i<20:
        sp[i]=i
    else:
        sp[i]=(i-6)*sp[i-7]
print((sp[47872]-290*sp[47865])/sp[47858])
