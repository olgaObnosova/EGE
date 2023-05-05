mx = 0
k = 0
with open('24(3).txt') as f:
    f = f.readline()
f = f.replace('C','*')
f = f.replace('D','*')
f = f.replace('F','*')
f = f.replace('A','^')
f = f.replace('O','^')
f = f.replace('**^','@')
f = f.replace('*^^','@')
for x in f:
    if x == '@':
        k+=1
        mx = max(mx,k)
    else:
        k = 0
print(mx)
