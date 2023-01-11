import random as rd 
mask1 = rd.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
mask2 = rd.randint(1, 10**9) 
ostatki = [] 
base = [] 
list = [] 
 
for i in range(10): 
     for j in range(10): 
         if int('12345'+ str(i) + '7' + str(j) + "8") % 23 == 0: 
             base.append(int('12345' + str(i) + '7' + str(j) + "8")) 
print(*base, sep = '\n') 
for x in range(len(base)): 
     ostatki.append(int(base[x] / 23)) 
print(ostatki)
