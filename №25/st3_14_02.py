import fnmatch as f
'''
for i in range(1072461,10**9):
    if i%4173==0:
        print(i)
        break
'''
for i in range(1072461,10**10,4173):
    if f.fnmatch(str(i),'1?7246*1'):
        print(i)