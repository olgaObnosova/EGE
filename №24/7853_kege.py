with open('24_7853.txt') as f:
    f=f.readline()
st = f[:2]
maxx=0
for i in range(2, len(f)):
    if not(st[-2] in 'NOT' and f[i] in 'NOT'):
        st+=f[i]
    else:
        maxx = max(maxx, len(st))
        st = st[-1]+f[i]
print(maxx)
