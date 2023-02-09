import fnmatch as f
for i in range(203405608, 10**9):
    if i%151==0:
        print(i)
        break
for i in range(203405758, 10**9, 151):
    if f.fnmatch(str(i),'2?34?56?8'):
        print(i, i//151)

