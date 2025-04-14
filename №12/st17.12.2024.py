sp=set()
for i in range(200):
    for j in range(200):
        s='21'*i
        while '111' in s or '22' in s:
            s=s.replace('111','2', 1)
            s = s.replace('222', '1', 1)
            s = s.replace('221', '1', 1)
            s = s.replace('122', '1', 1)
            s = s.replace('22', '2', 1)
        #print(s)
        if s.count('2')==9:
            sp.add(s)
print(sp)
