def divisors(digit):
    all_divisors = set()
    if digit%2==0:
        all_divisors.add(digit)
    for element in range(2, int(digit ** 0.5) + 1):
        if digit % element == 0 and element % 2 == 0:
            all_divisors.add(element)
        if digit % (digit // element) == 0 and (digit // element) % 2 == 0:
            all_divisors.add(digit // element)
    return all_divisors




for i in range(1, 100_000_000):
    n = 1_850_000_000 + i
    call = divisors(n)
    a = len(call)
    if a % 2 != 0:
        print(i, a)