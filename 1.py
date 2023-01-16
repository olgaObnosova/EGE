name = 'Петя'


def greet(name):
    global name
    print("Привет,", name)


greet('Вася')
print(name)
