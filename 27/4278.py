with open('primer.txt') as f:
    n=int(f.readline())
    sp=[int(x) for x in f]
spp=[0]*71
s=k=0
for x in sp:
    s+=x
    print(x, s, s%71, k)
    if s%71==0:
        k+=1
    k+=spp[s%71]
    spp[s % 71] += 1
print(k)

