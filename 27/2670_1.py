f = open('2670A.txt')
n = int(f.readline())
maxx=0
mibl=1500
for i in range(n):
  abc = [int(x) for x in f.readline().split()]
  maxx = max(abc)
  summ += maxx
  for x in abc:
    if (maxx - x) % 4 != 0 and maxx-x < minl:
      minl = maxx - x

print(summ,maxx)

if summ % 4 == 0:
  summ = summ - minl

if summ % 4 != 0:
  print( summ )
