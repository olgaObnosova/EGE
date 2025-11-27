with open('24_21.txt') as f:
    f=f.readline()
k=1
maxx = 0
for i in range(len(f)-1): #XYXZXXY
    if f[i]!=f[i+1]:
        k+=1
        maxx=max(maxx, k)
    else:
        k=1
print(maxx)