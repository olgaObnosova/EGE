i = 46 * '1' + 31*'2'
while '1111' in i:
    i = i.replace('1111', '2',1)
    i = i.replace('222', '1',1)
print(i)
a='gggg'
a=a.replace('5','i')
