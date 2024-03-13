s ='7' * 120
while '8887' in s or '77' in s:
    if '8887' in s:
        s = s.replace('8887','8',1)
    else:
        s = s.replace('77','8',1)
print(s)
