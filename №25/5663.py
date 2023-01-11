p+k = []
for i in range(161, 17 * (10 ** 6) + 1, 161):
    a = str(i)
    if '1' in a:
        fl = False
        for j in range(len(a) - 2):
            if a[j] == '1' and a.rfind('68') - j >= 3:
                fl = True
        if fl:
            pk.append(i)
for i in pk[::500]:
    print(i, i // 161)
