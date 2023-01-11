#https://kompege.ru/variant?kim=25006154
count=0
s='123456789'
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        t=a1+a2+a3+a4+a5+a6
                        if t[0]!='5' and t.count('2')==2:
                            count+=1
                        
    
print(count)    
