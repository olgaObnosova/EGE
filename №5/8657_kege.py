def tr(n):
    s=''
    while n!=0:
        s+=str(n%3)
        n=n//3
    return s[::-1]

for n in range(1,10000):
    z=tr(n)
    if n%5==0: #'100'- 100
        z=z+z[3:]
# z='102030'
# print(z[-3:])
    else:
        v=n%5
        v=v*5
        v=tr(v)
        z=str(z)+str(v)
    r=int(z,3)
    if r<5496:
        print(n)