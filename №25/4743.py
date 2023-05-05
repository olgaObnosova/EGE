m = []
def chislo(n):
    return 10_000_000 + n

def deliteli(n):
    spisok = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            spisok.add(i)
            spisok.add(n // i)
    b = sorted(list(spisok))
    if len(b) < 2:
        return [False, 0]
    else:
        if (b[-1] + b[-2]) < 100_000 and (b[-1] + b[-2]) % 31 == 0:
            return [True, b[-1] + b[-2]]
        else:
            return [False, b[-1] + b[-2]]
k = 0
for i in range(1, 1000000):
    if k == 5:
        break
    chislooo = chislo(i)
    m1 = deliteli(chislooo)
    if m1[0] == True:
        print(chislooo, m1[1])
        k += 1