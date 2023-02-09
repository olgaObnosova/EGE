sp = [0] * 2024
sp[1] = 1
for i in range(2, 2024):
    sp[i] = i * sp[i - 1]
print((sp[2023] - sp[2022]) // sp[2020])
