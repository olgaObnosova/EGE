m = []

def deliteliProst(n):
    spisok = set()
    isTrue = False
    qqq = set()
    for g in range(2, int(n ** 0.5) + 1):
        if n % g == 0:
            if g > 999:
                spisok.add(g)
            if (n // g) > 999:
                spisok.add(n // g)
            if g < 1000:
                qqq.add(g)
            if (n // g) < 1000:
                qqq.add(n // g)
    spisok = list(spisok)
    qqq = list(qqq)
    for kkek in qqq:
        if prostDeliteli(kkek):
            isTrue = True
            break


    if len(spisok) > 0 and isTrue == False:
        if prostDeliteli(min(spisok)):
            return [True, min(spisok)]
    return [False, 0]
k = 0
def prostDeliteli(n):
    for q in range(1, int(n ** 0.5) + 1):
        if n % q == 0 and q != 1 and q != n:
            return False
    return True

for i in range(121332132, 20222022, -1):
    if k == 5:
        break
    mmmmm = deliteliProst(i)
    if mmmmm[0]:
        print(i, mmmmm[1])
        k += 1
