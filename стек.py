# -*- coding: utf-8 -*-
f = open('input.txt','r')
otv = open('output.txt','w')
sp = []
t = 0
while True:
    s = f.readline()
    
    if not s:
        break
    if s[0] == '+':
        sp.append(s[1:].rstrip())
    elif s[0] == '-':
        if len(sp)==0:
            t=1
            break
            sp.pop()
    else:
        t = 1
        
if t == 1:
    otv.write('ERROR')   
elif len(sp) == 0:
    otv.write('EMPTY')
else:
    otv.write(' '.join(sp))
