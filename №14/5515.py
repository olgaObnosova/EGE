for a in range(55):
    if ((36*55**3 + a*55**2 +35*55+34) - (2*55**3 + 34*55**2 +a*55+35))%29==0:
        print(a)
print(((36*55**3 + 48*55**2 +35*55+34) - (2*55**3 + 34*55**2 +48*55+35))-\
              ((36*55**3 + 19*55**2 +35*55+34) - (2*55**3 + 34*55**2 +19*55+35)))  
