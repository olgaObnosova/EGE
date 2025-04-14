def f(n):
    s = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and i != (n//i):
            s.append(i)
            s.append(n//i)
        elif n%i == 0 and i == (n//i):
            s.append(i)
    if len(s) > 0:
        return max(s) + min(s)
    else:
        return 0
k = 0
for x in range(1000000, 0, -1):
    m = f(x)
    if k == 5:
        break
    if m % 100 == 18:
        print(x, m)
        k = k + 1