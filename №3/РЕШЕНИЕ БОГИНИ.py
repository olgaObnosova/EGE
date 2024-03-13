file = open("123.csv", encoding="utf-8-sig")
counter = 0
for line in file:
    stroka = [int(i.strip("\n")) for i in line.split(",")]
    two = []
    one = []
    for i in stroka:
        if i not in two and stroka.count(i) == 2:
            two.append(i)
        if i not in one and stroka.count(i) == 1:
            one.append(i)
    if len(two) == 3 and len(one) == 1 and (min(two) + max(two)) / 2 < one[0]:
        counter += 1
print(counter)



