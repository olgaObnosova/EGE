a='1'*2018+'2'*2019
while '111' in a:
    a = a.replace('111','2',1)
    a = a.replace('222', '1', 1)
print(a)