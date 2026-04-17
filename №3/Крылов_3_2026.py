with open('3_кр_2026') as f:
    sp = [[int(x) for x in line.split()] for line in f]
    k=0
    for line in sp:
        k+=1
        pov=[x for x in line if line.count(x)==2]
        npv=[x for x in line if line.count(x)==1]
        if len(pov)==4 and len(npv)==2: #1 1 2 2
            if sum(npv)<=sum(set(pov)): # 1 2
                print(k, line, sum(line))