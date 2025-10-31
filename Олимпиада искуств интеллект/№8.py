import csv as r

count = 0
with open('input.csv', 'r') as file:
    sp = r.reader(file)
    for line in sp:
        f1, f2, f3 = map(int, line)
        s = f1 + f2 + f3
        if 3 <= s <= 7:
            count += 1
print(count)