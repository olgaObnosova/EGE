with open('24_10105.txt') as f:
    f=f.readline().split('T')
    sp=[len(x) for x in f]
cnt = [sum(sp[i:i+101]) for i in range(len(sp))]
print(max(cnt) + 100)