for i in range(3, 10_000):
    s = '3'+i*'1'
    while '31' in s or '211' in s or '1111' in s:
        s=s.replace('31', '1', 1)
        s = s.replace('211', '13', 1)
        s = s.replace('1111', '2', 1)
    sm=0
    for x in s:
        sm+=int(x)
    if sm==15:
        print(i)
        break