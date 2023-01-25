f = open('2z.txt')
lines = f.readlines()
n = 0
mx = 0
for i in range(len(lines)-1):
    a = int(lines[i])
    b = int(lines[i+1])
    s7 = ''
    sm = a + b
    while sm > 0:
        s7 += str(sm % 7)
        sm //= 7
    s7 = s7[::-1]
    poly = True
    for j in range(len(s7)//2):
        if s7[j] != s7[len(s7)-j-1]:
            poly = False
            break
    if poly:
        n += 1
        if int(s7) > mx:
            mx = int(s7)
print(n, mx)
