def pov(st, sim):
    sl=dict()
    for i in range(len(st)-1):
        if st[i]==sim:
            if st[i+1] not in sl:
                sl[st[i+1]]=1
            else:
                sl[st[i + 1]] += 1
    return sorted(sl.items())
print(pov('abacaba', 'a'))
strok = input()
q = int(input())
buk = input().split()
for x in buk:
    otv = pov(strok, x)
    otv.sort(key = lambda x:x[1], reverse=True)
    print(otv[0][0], end=' ')

