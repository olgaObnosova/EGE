s='2'+140*'3'
while '2' in s:
    if '23' in s:
        s=s.replace('23', '3332')
    else:
        s = s.replace('2', '333')
print(sum([int(x) for x in s]))