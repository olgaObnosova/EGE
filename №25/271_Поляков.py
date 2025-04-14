def divisors(digit):
    all_divisors = set()
    for element in range(2, int(digit ** 0.5) + 1):
        if digit % element == 0:
            if (digit % element) % 7 == 0:
                all_divisors.add(element)
            if (digit // element) % 7 == 0:
                all_divisors.add(digit // element)
    return all_divisors


break_point1 = 0
for i in range(100_000_000, 1_000_000_000):
    call1 = divisors(i)
    if break_point1== 5:
        break
    if len(call1) == 15:
        print(i, max(call1))
        break_point1 += 1

break_point2 = 0
for i in range(1_000_000_000, 100_000_000,-1):
    call2 = divisors(i)
    if break_point2 == 5:
        break
    if len(call2) == 15:
        print(i, max(call2))
        break_point2 += 1