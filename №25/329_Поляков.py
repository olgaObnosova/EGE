def f(n):
    sp = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            sp.add(i)
            sp.add(n//i)
    sp = list(sp)
    if len(sp) >= 2:
        return (min(sp) + max(sp))
cnt = 0
for n in range(800000, 900000):
    m = f(n)
    if m != None:
        if m % 10 == 4:
            cnt += 1
            print(n, m)
            if cnt == 5:
                break