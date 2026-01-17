for n in range(96, 1000):
    r=bin(n)[2:]
    for i in range(3):
        if r.count('0')==r.count('1'):
            r+=r[-1]
        else:
            if r.count('0')<r.count('1'):
                r+='0'
            else:
                r+='1'
    r=int(r, 2)
    if r%4==0:
        print(n)
        break
