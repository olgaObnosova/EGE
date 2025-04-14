def f(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            s.add(i)
            if (n//i)%2 != 0:
                s.add(n//i)
    if len(s) < 999:
        return 0
    return sorted(list(s))
k = 0

for i in range(202_22_022 - 1, 121_332_132, -1):
    if k == 5:
        break
    m = f(i)
    if m != 0:
        if m[-5] > 0:
            k += 1
            print(m[-5], len(m))
