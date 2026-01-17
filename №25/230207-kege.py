def dl(n):
    s = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
def pr(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(1324728, 10 ** 10):
    d = dl(i)
    if len(d) == 1 and pr(d[0]):
        if str(d[0]).count('5') == 1:
            print(i, d)
    if len(d) == 2 and pr(d[0]) and pr(d[1]):
        if str(d[0]).count('5') == 1 and str(d[1]).count('5') == 1:
            print(i, d)
