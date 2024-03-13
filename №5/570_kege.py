maxx=0
for i in range(256):
    n=bin(i)[2:]
    n=(8-len(n))*'0'+n
    n1=n[::-1]
    r=int(n, 2)-int(n1,2)
    maxx=max(maxx, r)
print(maxx)
