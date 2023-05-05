from fnmatch import fnmatch

def prostDeliteli(n):
    spisochek = set()
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            spisochek.add(j)
            spisochek.add(n // j)
    spisochek = sorted(list(spisochek))
    spisochek.pop(-1)
    if len(list(spisochek)) % 2 == 0:
        return [True, max(spisochek)]
    return [False, 0]

for i in range(1, 10 ** 7):
    if fnmatch(str(i), "3*52?"):
        l = prostDeliteli(i)
        if l[0]:
            print(i, l[1])