with open('17_19249.txt') as f:
     sp=[int(x) for x in f]
# maxx=0
# for x in sp:
#     if len(str(abs(x)))==5 and str(x)[-2:]=='43':
#         maxx=max(maxx, x)
# print(maxx)
# cnt=0
# for i in range(len(sp)-2):
#     k=0# 9999<abs(sp[i])<100_000
#     if (len(str(abs(sp[i])))==5 and str(sp[i])[-2:]=='43'):
#         k+=1
#     if (len(str(abs(sp[i+1])))==5 and str(sp[i+1])[-2:]=='43'):
#         k+=1
#     if (len(str(abs(sp[i+2]))) == 5 and str(sp[i+2])[-2:] == '43'):
#         k += 1
#     if k>=1 and (sp[i]**2+ sp[i+1]**2+sp[i+2]**2)<=maxx**2:
#         cnt+=1
# print(cnt)