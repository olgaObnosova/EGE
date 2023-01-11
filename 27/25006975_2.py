f = open('25006975A.txt')
n=int(f.readline())
s = 0
i=0
mins = {0: (0, 0)}
res = []
for line in f:
    s += int(line)
    i+=1
    if s % 69 in mins:
        res += [(s - mins[s % 69][0], mins[s % 69][1] - i)]
    else:
        mins[s % 69] = (s, i)
print(mins)
print(res)
print(-max(res)[1])
