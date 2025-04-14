from re import findall

file = ''.join(open('24_18937.txt'))
first_num = r'(?:[1-9]{1}[0-9]{0,}|0)'

znak = r'(?:\+|\*){1}'
res = findall(rf'(?:{first_num}{znak})*', file)
res.sort(key=len)
print(res)