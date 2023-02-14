import fnmatch as f
for i in range(103456709, 10**9):
    if f.fnmatch(str(i),'1?34567?9') and i%17==0:
        print(i, i//17)