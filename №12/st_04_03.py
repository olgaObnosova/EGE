sp=set()
for i in range(1, 1000):
    s='1'*i
    while '111' in s or '222' in s:
        s=s.replace('111','22',1)
        s = s.replace('222', '11', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('22', '1', 1)
    sp.add(s)
print(sp)
