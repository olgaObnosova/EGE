def f(n):
  s = set()
  ch = {2, 4, 6 , 8}
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0 and (set(int(x) for x in list(str(i)))  - ch) == set():
      s.add(i)
      if (set(int(x) for x in list(str(n // i)))  - ch) == set():
        s.add(n // i)
  return s


k = 0

for i in range(400_000_000, 1000_000_000_000):
  if k == 5:
    break
  m = f(i)
  if len(m) > 6:
    n = sorted(list(m))[-6]
    print(n, len(m))
    k += 1
