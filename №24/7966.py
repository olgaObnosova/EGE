from re import *

s = open('24-310.txt').readline()
num = r'(?:[12][012]*|0)'
patten = rf'{num} (?:[+*] {num}) *'.replace(' ', '')

res = sorted(findall(patten, s), reverse=1, key=len)
for c in res:
    print(len(c), c)
    input()