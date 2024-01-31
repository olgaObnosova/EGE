s=0
for a in range(1, 500):
    f=1
    for x in range(1, 1000):
        f*=((x%a!=0)<=((x%120==0) or (x%180!=0)))
    if f:
        s+=a
print(s)