import fnmatch as f
for i in range(1021394, 10**9):
    if i%3052==0:
        print(i)
        break
for i in range(1022420, 10**10, 3052):
    if f.fnmatch(str(i), '1?2139*4'):
        print(i, i//3052)
def f(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True