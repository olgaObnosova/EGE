import string as s
alf=s.digits +  s.ascii_uppercase
print(alf.find('R'))
def c(n, b):
    n=n[::-1]
    s=0
    for i in range(len(n)):
        s+=n[i]*b**i
    return s
for x in range(19):
    a=c([9,8,8,9,7,x,2,1], 19)
    b=c([2, x, 9, 2, 3], 19)
    if (a+b)


