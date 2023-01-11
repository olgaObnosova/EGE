a = open('11.txt')
q = [int(i) for i in a]
fact = []
sp = []
for i in range(len(q)):
    if abs(q[i]) % 12 == 0:
        fact.append(q[i])
print(max(fact))
for i in range(len(q)-1):
    if (q[i]) % max(fact) == 0 or (q[i+1]) % max(fact) == 0:
        sp.append([q[i]+q[i+1]])
print(len(sp), *max(sp))
