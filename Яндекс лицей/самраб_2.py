dl = float(input())
tol = float(input())
pit = float(input())
eda = float(input())
t = float(input())
s = eda / (t * 60)
if dl >= s:
    print('Самая длинная змея', end=' ')
if tol >= s:
    print('Самая толстая змея', end=' ')
if pit >= s:
    print('Питончик')
