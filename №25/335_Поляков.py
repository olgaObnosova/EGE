def f(n):
  s = set()
  for i in range(2, int(n)):
    if n % i == 0 and i % 10 == 9 and i != 9:
      s.add(i)
      if (n // i) % 10 == 9 and (n // i) != 9:
        s.add(n // i)
  return s


k = 0
for i in range(800_001, 1000_000):
  if k == 5:
    break
  m = f(i)
  if m:
    print(i, min(m))
    k += 1
