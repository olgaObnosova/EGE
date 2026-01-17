with open('9_1.txt') as f:
    sp = [[int(x) for x in line.split()]\
          for line in f]
k=0
cnt=0
for line in sp:
    k+=1
    pov = [x for x in line if line.count(x)==3]
    npv = [x for x in line if line.count(x) == 1]
    if len(pov)==3 and len(npv)==4:
        if sum(npv)/len(npv)<=pov[0]:
            cnt+=1
            print(k, line, sum(line))
print(cnt)