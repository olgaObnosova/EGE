m=278
for n in range(1, 300):
    otv=m|n
    if bin(otv)[2:].count('1')==7:
        print(n)
        break
