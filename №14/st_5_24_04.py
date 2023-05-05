print(int('12',6)*int('34',6))
n=176
s=''
while n>0:
    s+=str(n%6)
    n=n//6
print(s[::-1])
print(int('54',6))