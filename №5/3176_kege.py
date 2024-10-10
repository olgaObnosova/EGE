def pyt(n):
    s = ''
    while n!=0:
        s+=str(n%9)
        n=n//9
    return s[::-1]
def cif(m):
    sp=[0]*9
    for x in m:
        t = m.count(x)
        sp[int(x)] = t
    g=max(sp)
    for i in range(len(sp)-1, 0, -1):
        if g==sp[i]:
            otv=i
            break
    return otv
print(cif('1222333'))
'''
for i in range(9999, 0, -1):
    n = pyt(i)
    k5=n.count('5')
    k7 = n.count('7')
    if k5==k7:
        n=n+n[-1]
    '''

