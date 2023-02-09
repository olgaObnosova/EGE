
with open('5988_kege.txt',encoding='unicode') as f:
    sp=[]
    for line in f:
        a=int(line.split()[0])
        b=line.split()[1]
        sp.append((a,b))
print(sp)