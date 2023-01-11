n=0
str='AB123'
for s1 in str:
  for s2 in str:
    for s3 in str:
      for s4 in str:
        for s5 in str:
            for s6 in str:
                for s7 in str:
                    for s8 in str:
                          if (s1+s2+s3+s4+s5+s6+s7+s8).count('A')+(s1+s2+s3+s4+s5+s6+s7+s8).count('B')==2:
                                n+=1
print(n)
