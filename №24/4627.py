with open('24_4627.txt') as f:
    s=f.readline()
s=s.replace('NPO','*')
s=s.replace('PNO','*')
k=mx=0
for x in s:
    if x=='*':
        k+=1
        mx=max(mx,k)
    else:
        k=0
print(mx)