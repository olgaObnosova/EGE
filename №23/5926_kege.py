import sys as s
s.setrecursionlimit(1_000_000) #AABC
def f(s, k, t):
    global st
    if k==24 and 'AA' not in t\
        and 'BB' not in t and 'CC' not in t:
        st.add(s)
        return s
    elif 'AA'  in t\
        or 'BB'  in t or 'CC'  in t:
        return  0
    f(s+1, k+1, t + 'A')
    f(s + 7, k + 1, t + 'B')
    f(s *4, k + 1, t + 'C')

st=set()
print(f(1, 0, ''))
print(len(st))

