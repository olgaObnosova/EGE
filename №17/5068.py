def sh(n):
    s=''
    while n > 0:
        s += str(n % 6)
        n = n // 6
    return len(s)


with open('5068.txt') as f:
    sp = [int(x) for x in f]
maxx =maxx2= k = 0
minn = float('inf')
for i in range(len(sp) - 2):
    if (sp[i] % 5 == 1 or sp[i + 1] % 5 == 1 or sp[i + 2] % 5 == 1) \
            and sh(sp[i]) == 4 and sh(sp[i + 1]) == 4 \
            and sh(sp[i + 2]) == 4:
        k += 1
        maxx2 = max(maxx2,(max(maxx, sp[i], sp[i + 1], sp[i + 2])-\
               min(minn, sp[i], sp[i + 1], sp[i + 2])))
print(k, maxx2)
