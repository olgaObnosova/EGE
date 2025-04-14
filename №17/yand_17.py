with open('17_y.txt') as f:
    sp = [int(x) for x in f]
minnnnnnn = 1000000000000000
count = 0
summ = []
for element in sp:
    if len(str((element))) == 3:
        if str(element)[-1] == '8' and element < minnnnnnn:
            minnnnnnn = element
print(minnnnnnn)
for i in range(len(sp) - 2):
    p1 = sp[i] ** 2 > minnnnnnn ** 2
    p2 = sp[i + 1] ** 2 > minnnnnnn ** 2
    p3 = sp[i + 2] ** 2 > minnnnnnn ** 2
    q1 = len(str(abs(sp[i]))) == 3
    q2 = len(str(abs(sp[i + 1]))) == 3
    q3 = len(str(abs(sp[i + 2]))) == 3
    if p3 + p2 + p1 == 2 and q1 + q2 + q3 >= 1:
        count += 1
        summ.append(sp[i] + sp[i + 1] + sp[i + 2])
print(count, max(summ))