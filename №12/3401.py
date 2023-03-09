a=86*'7'
while '4444' in a or '7777' in a:
    if '4444' in a:
        a=a.replace('4444', '77',1)
    else:
        a = a.replace('7777', '44', 1)
print(a)