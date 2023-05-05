def deliteli(n):
    maxChet = 0
    maxNechet = 0
    m = []
    for l in range(2, int(n ** 0.5) + 1):
        if n % l == 0:
            m.append([n // l, l])
            if l % 2 == 0:
                maxChet = max(maxChet, l)
            elif l % 2 == 1:
                maxNechet = max(maxNechet, l)
            if ((n // l) % 2) == 0:
                maxChet = max(maxChet, n // l)
            elif ((n // l) % 2) == 1:
                maxNechet = max(maxNechet, n // l)
    if maxChet == 0 or maxNechet == 0:
        return [False, 0]
    A = abs(maxChet - maxNechet)
    lll = deliteliProst(A)
    if lll == 0 and str(A)[-1] == "9":
        return [True, A]
    return [False, 0]


def deliteliProst(n):
    spisok = set()
    for g in range(2, int(n ** 0.5) + 1):
        if n % g == 0:
            spisok.add(g)
            spisok.add(n // g)
    return len(list(spisok))
k = 0
for i in range(250157, 10000000):
    jjj = deliteli(i)
    if k == 5:
        break
    if jjj[0]:
        print(i, jjj[1])
        k += 1