import itertools as t
k=0
s=list(t.permutations('0123456789abcdefghijklmnopqrstuvwxyz',r=3))
for x in s:
    x=''.join(x)
    if x[0]!='0':
        x=x.replace('0','*')
        x = x.replace('2', '*')
        x = x.replace('4', '*')
        x = x.replace('6', '*')
        x = x.replace('8', '*')
        x = x.replace('a', '*')
        x = x.replace('c', '*')
        x = x.replace('e', '*')
        x = x.replace('g', '*')
        x = x.replace('i', '*')
        x = x.replace('k', '*')
        x = x.replace('m', '*')
        x = x.replace('o', '*')
        x = x.replace('q', '*')
        x = x.replace('s', '*')
        x = x.replace('u', '*')
        x = x.replace('w', '*')
        x = x.replace('y', '*')
        x = x.replace('1', '@')
        x = x.replace('3', '@')
        x = x.replace('5', '@')
        x = x.replace('7', '@')
        x = x.replace('9', '@')
        x = x.replace('b', '@')
        x = x.replace('d', '@')
        x = x.replace('f', '@')
        x = x.replace('h', '@')
        x = x.replace('j', '@')
        x = x.replace('l', '@')
        x = x.replace('n', '@')
        x = x.replace('p', '@')
        x = x.replace('r', '@')
        x = x.replace('t', '@')
        x = x.replace('v', '@')
        x = x.replace('x', '@')
        x = x.replace('z', '@')
        if '@@' not in x and '**' not in x and x.count('*')>x.count('@'):
            k+=1
print(k)





