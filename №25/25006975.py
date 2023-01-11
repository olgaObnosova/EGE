def f(a):
    if a**0.5==int(a**0.5):
        sp=set()
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                sp|={i,a//i}
        return len(sp)
sr=[]
for i in range(159264873,973146285+1):
    if i**0.5==int(i**0.5):
        sr.append((f(i),i))
for i in range(1,len(sr),2000):
    print(sr[i])
