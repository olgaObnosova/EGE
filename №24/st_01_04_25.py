from re import * #51
with open('24st_01_04.txt') as f:
    f=f.readline()
patten = r'(?:[1-5][0-5]*|0)(?:[*][1-5][0-5]*|[*]0)*(?:[-][1-5][0-5]*|[-]0)*'
res = sorted(findall(patten, f), key=len, reverse=True)
k=0
for c in res:
    print(len(c), c)
    k+=1
    if k==5:
        break
print(f.index('1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1'))
print(f[6463620:6463800])