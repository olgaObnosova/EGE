import fnmatch as f


def syst(n, l):
    s = ''
    alf = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n > 0:
        if n % l < 10:
            s += str(n % l)
        else:
            s += alf[n % l]
        n = n // l
    return s[::-1] == s


for i in range(2023, 2023 ** 2):
    k = 0
    summ = 0
    if f.fnmatch(str(i), '20*23'):
        for j in range(2, 37):
            if syst(i, j):
                k += 1
                summ += j
    if k >= 2:
        print(i, summ)
