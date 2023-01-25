a = open('17.txt').readline()
count = 0
maxx= 0
ind = 0
for i in range(len(a)):
    if a[i] == 'C' and a[i + 1] =='C':
        count +=1
        if count > maxx:
            maxx = count
            ind = i
    else:
        count = 1

print(maxx)

