with open('26var01.txt') as f:
    n, m = f.readline().split()
    kom=[]
    sam=[]
    for i in range(int(n)):
        kom.append(int(f.readline()))
    for i in range(int(m)):
        sam.append(int(f.readline()))
sam.sort(reverse=True)
kom.sort(reverse=True)
pas=[]
for i in range(len(sam)):
    for j in range(len(kom)):
        if sam[i]>=kom[j] and kom[j] not in pas:
            pas.append(kom[j])
            break
print(len(pas))