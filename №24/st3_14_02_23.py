with open('24_st_3.txt') as f:
    maxx = 0
    maxx2 = 0
    n=0
    for line in f:
        k = 1
        b=''
        for i in range(len(line)-1):
            if line[i] == line[i + 1]:
                k += 1
                if  k > maxx:
                    maxx = k
                    b = line[i]
            else:
                k=1
        if b!='':
            n = line.count(b)
        if n > maxx2:
            maxx2 = n
            per =b

print(maxx2, per)
