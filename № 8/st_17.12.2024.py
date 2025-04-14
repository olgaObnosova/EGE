import string as s
st=s.ascii_lowercase
print(st)
num=st.find('f')*26**5+st.find('e')*26**4+st.find('d')*26**3+\
st.find('a')*26**2+st.find('b')*26**1+st.find('c')*26**0
print(num)
print(26+26**2+26**3+26**4+26**5+num)
