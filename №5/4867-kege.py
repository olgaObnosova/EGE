for n in range(1, 10_000):
    s = sum([int(x) for x in str(n) if int(x)%2==0]) #sum([]) '111'
    s2=0
    for i in range(len(str(n))):
        if i%2==1:
            s2=s2+int(str(n)[i])
    r = abs(s-s2)
    if r==9:
        print(n)

