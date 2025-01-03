"""(№ 4978) Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
ПОКА НЕ нашлось(00)
  заменить(01, 21022)
  заменить(02, 310)
  заменить(03, 230112)
КОНЕЦ ПОКА
Известно, что исходная строка начиналась с нуля и заканчивалась нулём, а между ними были только цифры 1, 2 и 3.
После выполнения данной программы получилась строка, содержащая 104 единицы, 39 двоек и 83 тройки.
Сколько цифр было в исходной строке?
Ответ: 28"""


def smallStr(s):
    while not "00" in s:
        s = s.replace('01', '21022', 1)
        s = s.replace('02', '310', 1)
        s = s.replace('03', '230112', 1)
    print(s.count("1"), s.count("2"), s.count("3"), s)


smallStr("010")  # 21313100            - 1: 3, 2: 1, 3: 2
smallStr("020")  # 3100                - 1: 1, 2: 0, 3: 1
smallStr("030")  # 232131312131313100  - 1: 7, 2: 3, 3: 6

a = []
for i in range(100):
    for j in range(100):
        for k in range(100):
            if (3 * i + 1 * j + 7 * k == 104 and 1 * i + 0 * j + 3 * k == 39 and 2 * i + 1 * j + 6 * k == 83):
                a.append(i + j + k)
print(min(a) + 2)