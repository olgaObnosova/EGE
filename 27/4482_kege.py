with open('4482A.txt') as f:
    sp = []
    n = int(f.readline())
    sp = [int(x) for x in f]
suml = sum(sp[:n//2])
sump = sum(sp[n//2:])
print(sump)
print(suml)
#for x in sp:
print(bin(151))
