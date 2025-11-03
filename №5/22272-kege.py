def pr(n):
    s = ''
    while n:
        s = s + str(n%9)
        n = n//9
    return s[::-1]
maxx=0
for n in range(1, 1000):
    r = pr(n) #766633312
    if r[0] =='7':
        r = r.replace('6', '*') #7***33312
        r = r.replace('3', '6') #7***66612
        r = r.replace('*', '3') #733366612
        r = '34' + r
    else:
        r = r+'45' #12345
        r = '3'+r[1:]
    r = int(r, 9)
    if r < 2876:
        print(r, n)
        if r >= maxx:
            maxx = r
            otv = n
print(otv)



