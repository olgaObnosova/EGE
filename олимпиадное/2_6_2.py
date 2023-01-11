a = int(input())
n = 2
s=[]
while n * n <= a:
    if a % n == 0 and n**0.5 == int(n**0.5):
        s.append(n)
    else:
        n+=1
print(max(s))
