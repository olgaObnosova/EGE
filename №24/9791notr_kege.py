with open('9791.txt') as f:
    f=f.readline()
ch='0123456789ABCDEF'
maxx=k=0
for x in f:
    if x in ch:
        k+=1
        maxx=max(maxx, k)
    else:
        k=0
print(maxx)