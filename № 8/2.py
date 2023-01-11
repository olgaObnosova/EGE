k = 0 
from itertools import * 
for j in range(3, 8): 
    for i in product('СЕПИЯ', repeat=j): 
        s = ''.join(i) 
        if s.count('Е')<=2 and s.count('И')<=2 \
            and s.count('Я')<=2 and (s[0]=='П'  or s[0]=='С' \
                and(s.count('П')==0 or s.count('C')==1)):
                                     k+=1 
print(k) 
 
