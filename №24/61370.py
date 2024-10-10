with open('24 (1).txt') as f:
    f=f.readline()
f = f.replace('A', 'A ')
f = f.replace('B', 'B ')
maxx=-float('inf')
f = f.split()
for i in range(len(f)-2):
    if 'A' in f[i] and 'B' in f[i+1]:
        lenn = len(f[i]) + len(f[i+1]) + (len(f[i+2])-1)
        maxx = max(maxx, lenn)
    if 'B' in f[i] and 'A' in f[i + 1]:
        lenn = len(f[i]) + len(f[i + 1]) + (len(f[i + 2]) - 1)
        maxx = max(maxx, lenn)
print(maxx)
