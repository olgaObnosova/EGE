import time
start = time.time()
sp=[]
with open('1') as f:
    for x in f:
        sp.append(int(x))
N = len(sp)
for i in range(N-1):
    for j in range(N-i-1):
        if sp[j] > sp[j+1]:
            sp[j], sp[j+1] = sp[j+1], sp[j]
end = time.time()
print(sp)
print((end-start) * 10**3, "ms")