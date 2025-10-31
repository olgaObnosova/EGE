
def pit(n):
    s=''
    while n!=0:
        s+=str(n%5)
        n=n//5
    return s[::-1]
minn=10000000000
for n in range(1,10000):
    z=pit(n)
    if len(z)%2==0:
        z1=z[:len(z)//2]
        z2=z[len(z)//2:]
        z3=z2+z1
        while z3[0]=='0':
            z3=z3[1:]
    else:
        n1=n%5
        z=z+str(n1)
        z1 = z[:len(z) // 2]
        z2 = z[len(z) // 2:]
        z3 = z2 + z1
    r=int(z3,5)
    if r > 50:
        minn=min(minn,n)
print(minn)