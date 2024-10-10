with open('def_2.txt') as f:
    f = f.readline()
f = f.split('U')
minn = float('inf')
for i in range(len(f)-99):
    d = 'U'+'U'.join(f[i:i+99])+'U'
    if len(d)<minn:
        otv=d
        minn=min(minn, len(d))
print(minn)
s=open('1.txt', 'w')
s.write(otv)
