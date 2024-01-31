for n in range(3, 1001):
    s='1'+ n *'8'
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s=s.replace('18','8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    if s.count('1') == 3:
        print(n)
        break

for n in range(101, 200):
    s = '1'* n
    while '111' in s:
        s=s.replace('111', '2', 1)
        s=s.replace('2222', '333', 1)
        s=s.replace('33', '1', 1)
    if s.count('1') == 0:
        print(n)
        break

s='4' * 204
while '4444' in s or '777' in s:
    if '4444' in s:
        s=s.replace('4444', '77', 1)
    else:
        s = s.replace('777', '4', 1)
print(s)
