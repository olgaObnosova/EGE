from re import * # ответ не правильный. Надо подумать!
with open('24_9753.txt') as f:
    f=f.readline()
reg =r'(?=((?:[^Y]|Y(?!(?:[^Y]*Y){150}))*))'
sp = findall(reg, f)
st = max(sp, key=len)
print(st)
print(len(st))