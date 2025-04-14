with open('26_9847.txt') as f:
    n=int(f.readline())
    sp=[[int(x) for x in line.split()] for line in f]
time = [0] * 1440
for st, end in sp:
    for i in range(st, end):
        time[i]+=1
maxx=max(time)
print(maxx)
print('______')
for i in range(1440):
    if time[i]==maxx:
        print(i)
