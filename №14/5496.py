for x in '0123456789a':
    for y in '0123456789a':
        a='7'+y+'23'+x+'5'
        b='67'+x+'9'+y
    if (int(a,25)+int(b,11))%131==0:
        print((int(a,25)+int(b,11))//131)
    
