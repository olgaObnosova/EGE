a = 53**123+65**2222-172**12
s = ''
while a > 0:
    s+=str(a%7)
    a = a // 7
s=s[::-1]
k=s.count('61') + s.count('62')+s.count('63') \
  + s.count('64') +s.count('65')

print(k)