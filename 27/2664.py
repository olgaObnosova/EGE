f = open('2664_B.txt')
n = int(f.readline())
print(n)
s =[0]

for i in range(n):
    chisla = [int(x) for x in f.readline().split()]
    #print('chisla',chisla)
    pari = [ a + b for a in chisla for b in s]
    #print(max(pari))
    s = {x%5:x for x in sorted(pari)}.values()
#print('s',s)

#print(max(pari))
m = max(x for x in pari if x % 5 == 0)
print(m)
