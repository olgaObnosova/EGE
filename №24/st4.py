f=open('24_st4.txt').readline().split('A')
k=0
for x in f:
    if len(x)>=10 and x.count('B')>=2:
        k+=1

print(k)
