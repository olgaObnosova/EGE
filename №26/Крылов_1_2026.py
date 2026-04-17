with open('26var01.txt') as f:
    n, m = f.readline().split()
    kom=[]
    sam=[]
    for i in range(int(n)):
        kom.append(int(f.readline()))
    for i in range(int(m)):
        sam.append(int(f.readline()))
print(len(kom), len(set(kom)))
sam.sort(reverse=True) # 100 90 80
kom.sort(reverse=True) # 101 99 80 80
pas=[]
for i in range(len(sam)):
    for j in range(len(kom)): # 99 80
        if sam[i]>=kom[j] and (kom[j], j) not in pas:
            pas.append((kom[j], j))
            break
print(len(pas), max(pas))