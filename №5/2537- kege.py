for n in range(1, 5000):
    smch=sum([int(x) for x in str(n) \
              if int(x)%2==0])
    snch = sum([int(str(n)[i]) \
                for i in range(1, len(str(n)),2)])
    r = abs(snch-smch) #1234
    if r==13:
        print(n)