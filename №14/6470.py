'''
sp = '0123456789abcdefghijklmnopqrstuvwxyz'
for p in range(7, 36):

    for x in sp[:p-1]:
        for y in sp[:p-1]:
            if int('161', p)*int('56',p)==int(f'5{x}{y}6',p):
                print(x,y)
'''
import time
start_time = time.time()


for p in range(7, 100):
    pr = (p ** 2 + 6 * p + 1) * (5*p+6)
    for x in range(100):
        for y in range(100):
            rez=5*p**3+x*p**2+y*p+6
            if pr==rez and x<p and y<p:
                print(x, y, p)
print(3*38+37) #151

print("--- %s seconds ---" % (time.time() - start_time))