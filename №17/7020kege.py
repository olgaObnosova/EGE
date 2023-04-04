f = open('17_7020.txt')
s = [int(i) for i in f.readlines()]
k=0
m=minn=float('inf')
for x in s:
    if x>0:
        m=min(m,x)
for x in range(len(s)-3):
    if abs(s[x]) % 111 != m \
            and abs(s[x+1]) % 111 != m\
            and abs(s[x+2]) % 111 != m \
            and abs(s[x+3]) % 111 != m:
        k+=1
        minn=min(s[x]+s[x+1]+s[x+2]+s[x+3], minn)
print(k, minn)