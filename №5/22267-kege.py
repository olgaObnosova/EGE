def sm (n):
    s=''
    while n:
        s+=str(n%7)
        n=n//7
    return s[::-1]
maxx=0
for n in range(1, 100_000):  #12*6**111 32*6**333
    r = sm(n)
    if r[-1]=='2':
        r = r.replace('3', '*')
        r= r.replace('1', '3')
        r=r.replace('*', '1')
        r = '21'+r
    else:
        r = r+'36'
        r ='1' + r[1:]
    r =int(r, 7)
    if r<744:
        if r>maxx:
            maxx=r
            otv =n
print(maxx, otv)
