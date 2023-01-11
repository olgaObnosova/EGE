n=int(input())
is_prime=[True]*(n+1)
d=2
while d*d<=n:
    if is_prime[d]:
        for i in range(d**2,n+1,d):
            is_prime[i]=False
    d+=1
x=int(input())
print(is_prime[x])
print(is_prime)
