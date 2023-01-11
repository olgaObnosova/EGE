def pyt(n):
    s=''
    while n>0:
        s+=str(n%5)
        n=n//5
    return s[::-1]
a=0
for i in range(1,1000):
    a=i
    b=125**200-5**a+74
    b=pyt(b)
   
    if b.count('4')==100:
        print(i)
