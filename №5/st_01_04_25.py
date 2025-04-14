def f(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]


maxx=0
for i in range(1000):
    n = f(i)
    s = n.count('1') + n.count('2') * 2
    if s % 3 == 0:
        n = '112' + n[2:]
    else:
        n = n + f(s)
    r= int(n, 3)
    if r<679 and r%2==0:
        maxx=max(maxx, r)
print(maxx)
print(52*1024*1024*1024*8/(8219*3852*1980))
print(50_324/7)