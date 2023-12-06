sp=[(5,5),(7,30),(8,7),(15,7),(11,19),(16,19),(17,10),(20,11),(3,4)]
for a in range(30):
    k=0
    for x in sp:
        s,t=x
        if s>a or t>25 or s==t:
            k+=1
    if k==4:
        print(a)


