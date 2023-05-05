from fnmatch import fnmatch
c =[]
for i in range(161, 17 * 10 ** 6, 161):
    if fnmatch(str(i), "*1?*?68*"):
        c.append(i)
for g in range(0,len(c)+1,500):
    print(c[g],c[g]//161)