with open('5805.txt') as f:
    f = f.readline().split('0')
maxx = 0
for x in f:
    s = 0
    for i in x:
        s += int(i)
    if s % 5 == 0 and len(x) > maxx:
        maxx = len(x)
        sm = s
print(sm)
print(s)
print(maxx)
