
f = list(map(int, open("primer.txt").read().split('\n')))
n = f[0]
f.pop(0)
a = [0] * n
if f[0] % 5 == 0 and (1 - (f[0] % 7 == 0)):
    a[0] = -1
elif f[0] % 7 == 0 and (1 - (f[0] % 5 == 0)):
    a[0] = 1

for i in range(1, n):
    if f[i] % 5 == 0 and (1 - (f[i] % 7 == 0)):
        a[i] = a[i - 1] - 1
    elif f[i] % 7 == 0 and (1 - (f[i] % 5 == 0)):
        a[i] = a[i - 1] + 1
    else:
        a[i] = a[i - 1]
    #print(a)
cout = 0
b = [0] * n
for i in range(n):
    cout += b[a[i]]
    b[a[i]] += 1
    if a[i] == 0:
        cout += 1
print(cout)
print(f)
print(a)
print(b)