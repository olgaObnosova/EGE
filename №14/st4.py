a=7*729**6+6*81**9+3**14-90
count=0
while a>0:
    if a%9%2==0:
        count+=1
    a=a//9
print(count)
