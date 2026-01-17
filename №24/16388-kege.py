with open('24_16388.txt') as f:
    f=f.readline()
#f=f.replace('KLMN', '****')
k=maxx=0
s=''
s2='KLMN'
for i in range(100):
    if s2*i in f:
        print(i)
print(4*45)
x = ''

while x + 'KLMN' in s:
    x += "KLMN"

if x + 'K' in s:
    x += 'K'
    if x + 'L' in s:
        x += 'L'
        if x + 'M' in s:
            x += 'M'
# for x in f:
#     if x=='*':
#         k+=1
#         s+=x
#         if k>maxx:
#             maxx=k
#             otv =s
#     else:
#         k=0
#         s=''
# print(maxx)
# print(f.index(otv))
# print(f[2587378-10:2587378+10+180])
