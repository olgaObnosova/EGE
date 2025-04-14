# import itertools as t
# l=list(t.product('12', repeat=20))
# for i in range(1, 20):
#     for x in l:
#         otv=x
#         x=''.join(x)
#         if x.count('1')==x.count('2'):
#             x='0'+x*i+'0'
#             while '00' not in x:
#                 x=x.replace('011', '20')
#                 x = x.replace('022', '10')
#                 x = x.replace('02', '110')
#                 x = x.replace('01', '220')
#             if x.count('1')==47 and x.count('2')<70:
#                 print(i* otv.count('2'))
# s=[]
# for a in range(50):
#     for b in range(50):
#         for c in range(50):
#             for d in range(50):
#                 if a*0+b*1+c*0+d*2==47\
#                     and 1*a+b*0+2*c+d*0 < 70 \
#                         and 2*a + c == 2*b + d:
#                     s.append(1*a+b*0+2*c+d*0)
# print(max(s))
sp=[]
for x in range(20):
    for y in range(20):
        for z in range(20):
            if 2*y+z==13 and 2*x+3*y+z==18:
                sp.append(x+y+z)
print(sp)