f=open("18-18")

d=[]
b=[float(x.replace(",",".")[0:-1]) for x in f]
for i in range(len(b)):
    try:
        FLAG = True
        indexx = (b.index(b[i]))+1
        summ = b[i]
        while FLAG == True:

            if b[i] < b[indexx]:
                summ += b[indexx]
                indexx += 1
                i+=1
            else:
                d.append(summ)
                FLAG = False
    except IndexError:

        print(int(max(d)))
        break










