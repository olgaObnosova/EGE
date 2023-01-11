def tri(n):
    s=''
    while n>0:
        s+=str(n%3)
        n=n//3
    return s[::-1]
def pyt(n):
    s=''
    while n>0:
        s+=str(n%5)
        n=n//5
    return s[::-1]
summ=0
for i in range(95):
    f=tri(i)
    d=pyt(i)
    if f[-2:]=='21' and d[0]=='3':
        summ+=i
print(summ)
