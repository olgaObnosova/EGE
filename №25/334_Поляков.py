M=100000000
s=set()
n=908220
for i in range(2, int(n**0.5)+1):
    if n%i==0:
        s.add(i)
        s.add(n//i)
        sm=sum(s)
    M=min(M, sm)
print(n, M)

#ОТвет 900220 450112
#      902220 451112
#      904220 452112
#      906220 453112
#      908220 454112
