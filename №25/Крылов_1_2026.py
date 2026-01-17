sp103=[]
sp3=[] #1032345
for i in range(1, 3000, 2):
    sp103.append(i*103)
print(sp103[-1])
for i in range(20):
    sp3.append(3**i)
print(sp3[-1])
sp=[]
for i in range(len(sp103)): #1500 103
    for j in range(len(sp3)): #20
        ch=sp103[i]+sp3[j]
        strc = str(ch)
        if len(strc)==6 and '1' not in strc:
            sp.append([ch, j])
sp.sort()
print(sp)
