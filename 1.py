x=int(input())
p=int(input())
y=int(input())
k=0
while y>x:
  x = trunc(x+x*p/100)
  x=int(x)


  k+=1
print(k)