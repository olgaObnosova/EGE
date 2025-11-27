'''?: - "ГРУППИРУЙ, НО НЕ ЗАПОМИНАЙ"
Простая аналогия: Как скобки в математике - они группируют вычисления, но сами не являются результатом.
Пример 1: Простая группировка'''
import re
text = "цвет color colour"
# Без ?: - запоминает ВСЁ
result1 = re.findall(r'(colou?r)', text)
print(result1)  # ['цвет', 'color', 'colour']

# С ?: - группирует, но не запоминает саму группу
result2 = re.findall(r'(?:colou?r)', text)
print(result2)  # ['цвет', 'color', 'colour'] - пока разницы нет
text = "test123 test456 example789"

# Хочу найти только цифры после "test"
# Без ?: - проблема!
result_bad = re.findall(r'(test\d+)', text)
print(result_bad)  # ['test123', 'test456'] - а мне нужны только цифры!

# С ?: - решение!
result_good = re.findall(r'(?:test)(\d+)', text)
print(result_good)  # ['123', '456'] - вот теперь только цифры!
text = "apple banana cherry orange"

# Найти фрукты, которые начинаются на a или c
result = re.findall(r'(?:a|c)\w+', text)
print(result)  # ['apple', 'cherry']

'''?= - "ПРОВЕРЬ, ЧТО ДАЛЬШЕ ЕСТЬ ЭТО, НО НЕ ВКЛЮЧАЙ В РЕЗУЛЬТАТ"'''

text = "100px 200em 300px 400rem"

# Найти числа, за которыми СЛЕДУЕТ "px"
result = re.findall(r'\d+(?=px)', text)
print(result)  # ['100', '300'] - только числа перед "px"

text = "test123 example test456"

print("?: - группируем 'test' с цифрами, но берем только цифры:")
result1 = re.findall(r'(?:test)(\d+)', text)
print(result1)  # ['123', '456']

print("\n?= - находим 'test', перед которым есть цифры:")
result2 = re.findall(r'\d+(?=test)', text)  # Ничего не найдет!
print(result2)  # []

print("\n?= - находим слова, после которых есть цифры:")
result3 = re.findall(r'test(?=\d+)', text)
print(result3)  # ['test', 'test']