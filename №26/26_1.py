file = open('26var01.txt').readlines()
# M - ГОРИЗОНТАЛЬНЫЕ РЯДЫ
# K - вертикальные ряды
N, M, K = [int(i) for i in file[0].split()]

# M, k
pari = [[int(i) for i in j.split()] for j in file[1:]]
slovar = {}
for m, k in pari:
    if k not in slovar.keys():
        slovar[k] = [m]
    else:
        slovar[k].append(m)
    slovar[k].sort()
slovar = dict(sorted(slovar.items(), key=lambda x:x[0]))
otvet = []
for k in range(1, K):
    # получаю соседние столбцы вертикальные
    st1, st2 = slovar[k], slovar[k + 1]

    # отсчет от верхней границы до первого корабля
    mka = min(min(st1), min(st2))
    otvet.append([mka - 1, k])
otvet.sort(key=lambda x:x[0], reverse=True)
print(otvet)