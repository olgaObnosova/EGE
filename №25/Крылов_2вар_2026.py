sp113=[]
sp3=[]
for i in range(113, 2*10**6, 113):
    if i%2!=0:
        sp113.append(i)
for i in range(15):
    sp3.append(3**i)
k=0
for i in range(111111, 10**10):
    if '0' not in str(i):
        for x in sp113:
            for j in range(1, len(sp3)):
                if i==x+sp3[j]:
                    k+=1
                    print(i, j)
                    break
        if k==5:
            break
