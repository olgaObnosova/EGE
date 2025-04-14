import fnmatch as f
# for i in range(30120145, 10**10):
#     if i%1917==0:
#         print(i)
#         break
for i in range(1917, 10**10, 1917):
    if f.fnmatch(str(i), '3?12?14*5') and i%1917==0:
        print(i, i//1917)