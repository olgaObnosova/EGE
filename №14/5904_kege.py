def sm(n):
    s=''
    while n:
        s+=str(n%7)
        n=n//7
    return s[::-1]
import string as s
alf = s.digits+s.ascii_lowercase[:10]
maxs=0
for x in alf:
    for y in '01234':
        a = int(f'{x}1{x}2{x}3{x}4', 20)
        b = int(f'1{y}2{y}3{y}4{y}', 5)
        r = a-b
        r = sm(r)
        summ = 0 # r = '1230234'
        for i in r:
            summ+=int(i)
        maxs = max(maxs, summ)
print(maxs)

