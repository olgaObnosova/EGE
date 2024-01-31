from fnmatch import fnmatch as f
a = 0
for i in range(2468035, 10**9):
    if i % 13 == 0:
        print(i)
        a = i
        break
s = '39'
for x in s:
    for i in range(a, 10**9, 13):
        if f(str(i), f'24*68{x}35'):
            print(i, i/13)