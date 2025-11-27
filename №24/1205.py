with open('24_1205.txt') as f:
    f=f.readline()
cnt=maxx2=0
for x in f: #AAWAAAAAAA
    if x not in 'GWP':
        cnt+=1
        maxx2=max(maxx2, cnt)
    else:
        cnt=0
print(maxx2)

f=f.replace('G', '*')
f=f.replace('W', '*')
f=f.replace('P', '*')
maxx=0
f=f.split('*')
print(len(max(f, key =len))) #max(['aaa', 'bbb', '453'])

for x in f:
    maxx=max(maxx, len(x))
print(maxx)