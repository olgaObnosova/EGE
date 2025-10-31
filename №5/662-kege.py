s = set()
for n in range(20, 601):
    r = bin(n)[2:] #123456
    r = r[:-2]
    r = int(r, 2)
    s.add(r) #s
print(len(s))