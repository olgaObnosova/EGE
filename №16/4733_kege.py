'''def f(n):
    if n==1:
        return 1
    else:
        return (2*n-1) * f(n-1)
print(f(3516)/f(3513))'''
sp=[0]*3517
sp[1]=1
for i in range(2,3517):
    sp[i]=(2*i-1)*sp[i-1]
print(sp[3516]/sp[3513])