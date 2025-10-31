alf = '0123456789'
k=0
for x1 in alf[1:]:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                x=x1+x2+x3+x4
                if x.count('0')<=1 and x.count('1')<=1\
                    and x.count('2')<=1 and x.count('3')<=1 \
                        and x.count('4') <= 1 and x.count('5') <= 1 \
                        and x.count('6') <= 1 and x.count('7') <= 1 \
                        and x.count('8') <= 1 and x.count('9') <= 1:
                    if int(x[0])%2!=int(x[1])%2 and int(x[1])%2!=int(x[2])%2\
                        and int(x[2])%2!=int(x[3])%2:
                        k+=1
print(k)

