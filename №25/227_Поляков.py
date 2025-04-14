def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        else:
            return True

c = 1
for n in range(2022, 200, -1):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0 and pr(i):
            break
    if i>10 and pr(i):
        c+=1
        print(n, i)
    if c>5:
        break

