def sm(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n = n // 7
    return s[::-1]


maxx = 0
with open('17_12746.txt') as f:
    sp = []
    for x in f:
        x = int(x)
        sp.append(int(x))
        x1 = sm(x)
        if x1[0] == '2':
            maxx = max(maxx, x)
maxx = maxx * 2
cnt=0
mins = float('inf')
for i in range(len(sp)-2):
    a1 = sm(sp[i])
    a2 = sm(sp[i+1])
    a3 = sm(sp[i+2])
    k=0
    if a1[-1]=='1':
        k+=1
    if a2[-1]=='1':
        k+=1
    if a3[-1]=='1':
        k+=1
    if k==2 and (sp[i]+sp[i+1]+sp[i+2] > maxx):
        cnt+=1
        mins=min(mins, sp[i]+sp[i+1]+sp[i+2])
print(cnt, mins)
