def pt(n):
    s=''
    while n!=0:
        s+=str(n%5)
        n=n//5
    return s[::-1]
maxx=0
for i in range(1, 1235):
    n=pt(i)
    if i%5==0:
        s5=sum([int(x) for x in str(i%52)])
        n=pt(s5)+n
    else:
        n=n[0]+n
    r=int(n, 5)
    maxx = max(r, maxx)
print(maxx)

