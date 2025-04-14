maxx=0
for i in range(10**9):
    n=bin(i)[2:]
    if n.count('0')>n.count('1'):
        nm=n.find('0')
        n=n[:nm]+'1'+n[nm+1:]
    else:
        nm = n.rfind('1')
        n = n[:nm] + '0' + n[nm + 1:]
    r=int(n, 2)
    rez=abs(r-i)
    print(i, rez)
    if rez>maxx:
        maxx=rez
        otv=i
print(otv)