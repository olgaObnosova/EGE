a = open("26.txt").readlines()
c = []
for i in a:
    c.append([int(i.strip().split(" ")[0]), int(i.strip().split(" ")[1])])
k = {}
kbebra = {}
for i in c:
    if i[1] in k:
        k[i[1]].append(i[0])
        kbebra[i[1]] = kbebra[i[1]] + 1
    else:
        k[i[1]] = [i[0]]
        kbebra[i[1]] = 1
mishaKrash = []
originalKey = 0
for i in kbebra.keys():
    if kbebra[i] == max(kbebra.values()):
        originalKey = i
print(originalKey, "Первый ответ")
for i in k[originalKey]:
    mishaKrash.append(int(str(i)[:-1]))

kmax = 0
print(len(set(mishaKrash)), "Второй ответ")
