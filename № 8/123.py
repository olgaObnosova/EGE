count=0
for x1 in '0123456':
    for x2 in '0123456':
        for x3 in '0123456':
            for x4 in '0123456':
                for x5 in '0123456':
                    for x6 in '0123456':
                        for x7 in '0123456':
                            x=x1+x2+x3+x4+x5+x6+x7
                            if x[0]!='0' and x[0]!='3' and x[0]!='5'\
                               and not ('22' in x and '44' in x):                             
                               
                                    count+=1
print(count)
    
