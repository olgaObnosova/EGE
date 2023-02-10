a=int(input())
b=-1
b2=-1
while a>0:
  if a%10>=b:
    b2=b
    b=a%10
  elif a%10>b2:
    b2=a%10
  a=a//10
print(b, b2)