def s(n):
    e = set()
    sp = []
    count = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            e.add(i)
            e.add(n//i)
    sp = list(e)
    sp.sort()
    for k in sp:
        count += k
    if str(count) == str(count)[::-1]:
        return count
    return 0

count1 = 0
for g in range(520000, 10**10):
    t = s(g)
    if t:
        count1 += 1
        print(g, t)
    elif count1 == 5:
        break