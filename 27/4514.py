f = open("4514A.txt")

n = int(f.readline())
chet = 0
s = 0
sp = [10 ** 9] * 13
maxs = 0
for line in f:
    line = int(line)
    s += line
    if line % 2 != 0:
        chet += 1
    if chet % 13 == 0:
        maxs = max(maxs, s)
    else:
        maxs = max(maxs, s - sp[(chet - 13) % 13])
    sp[chet % 13] = min(sp[chet % 13], s)
print(maxs)
