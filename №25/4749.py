def S(number):
    divs = []
    div = 2
    while (div * div <= number) and len(divs) < 4:# возможно не кладет после корня
        if number % div == 0:
            if number // div not in divs: #  если кв изв, то я не кладу ни одну
                divs = divs + [number // div]
        div += 1
    if len(divs) == 3: return sum(divs)
    else: return 0

A = []
for i in range(10, 100):
    if str(i)[0] > str(i)[1]:
        A.append(str(i))
print(A)
count=0
for i in range(10_000_001, 99**99): #111
    f = 1
    
    s = S(i)
    if s:
        s = str(s)
        for j in range(len(s)-1):
            print(s)
            print(s[j:j+2])
            if s[j:j+2] in A:
                f = 0
                break
        if f:
            count+=1
            print(i, s)
        if count==5:
            break
            
