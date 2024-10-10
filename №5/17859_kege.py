def pt(n):
    s=''
    while n!=0:
        s+=str(n%5)
        n=n//5
    return s[::-1]
m=0
for i in range(1, 13):
    N = bin(i)[2:]
    if i%2==0:
        N='10'+N
    else:
        N='1'+N+'01'
    R=int(N, 2)
    m=max(m, R)
print(m)


