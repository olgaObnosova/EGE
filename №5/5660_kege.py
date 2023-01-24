k=0
for i in range(100,201):
    num = bin(i)[2:]
    if len(num)%2==0:
        num = num + '10'
    else:
        num = '11' + num
    num = int(num,2)
    if num%2==0:
        k+=1
print(k)