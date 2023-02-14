with open('5940_kege.txt') as f:
    n=int(f.readline())
    sp=[[]]*500
    p=[]
    for line in f:
        a,b,c = map(int,line.split())
        p.append(a)
        sp[a]=[b,c]
p.sort()
#print(p)
print(sp)
num=[11]
summ=[]

k=12
while k<200:
    k+=1
    if num[-1] in p:
        if  sp[num[-1]+1][0]<sp[num[-1]+1][1] \
                and (num[-1]+1) in p and (num[-1]+1) not in num:
            num.append(num[-1]+1)
            summ.append(sp[num[-1]+1][0])

        elif (num[-1]+2) in p and (num[-1]+2) not in num:
            num.append(num[-1] + 2)
            summ.append(sp[num[-1] + 2][1])
        elif (num[-1]+1) in p:
            num.append(num[-1] + 1)
            summ.append(sp[num[-1] + 1][0])
s=0
print(num)
print(summ)



