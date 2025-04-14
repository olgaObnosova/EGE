
def ch(n):
    s=''
    while n!=0:
        s+=str(n%4)
        n=n//4
    return s[::-1]
minn = 9999999
for i in range(1, 10_000):
    n = ch(i)
    if i%2==0:
        ml = int(n[-1], 4) *3
        ml = ch(ml)
        n = '12'+ n + ml
    else:
        n = '13' + n + '21'
    r = int(n, 4)
    if r>50:
        minn= min(minn, r)
print(minn)