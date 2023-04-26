
def delit(n):
    s=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return sum(s)+1
def dr(a,b):

    if delit(a) ==b and  delit(b)==a:
        return a,b
    return 0
f=1
a, b = map(int, input().split())
for i in range(a,b-1):
    for j in range(i+1, b):
        if dr(i,j):
            f=0
            print(dr(i,j))
if f:
    print(0)
