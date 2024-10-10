def pyt(n):
    s = ''
    while n!=0:
        s+=str(n%5)
        n=n//5
    return s[::-1]
for i in range(1000, 0, -1):
    n = pyt(i)
    posl= n[-1]
    if int(posl)%2==0:
        n = n + '2'
    else:
        n = '2' + n + '3'
    r = int(n, 5)
    if r < 1000:
        print(i)
        break
