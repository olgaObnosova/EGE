a=3*125**6+2*25**9+5**12-625
count=0
while a>0:
    if a%5==0:
        count+=1
    a=a//5
print(count)
