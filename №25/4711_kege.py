import fnmatch as f

for i in range(1021395, 9999999):
    if i % 2023 == 0:
        print(i)
        break
for i in range(1021615,10**10,2023):
    if f.fnmatch(str(i),'1?2139*4'):
        print(i)