def f(x,y, k):
	if x>y or k>3:
		return 0
	elif x == y and k<=3:
		return 1
	return f(x+1,y, k+1) + f(x+2, y, k+1) + f(x*3,y, k+1)
s=0
for y in range(4, 1000, 2):
	s+=f(4, y, 0)
print(s)