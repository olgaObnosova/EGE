name = 'Петя'
print(id(name))
print(name)
def greet(name):
    print(name)
    print((id(name)))
    #print("Привет,", name)

greet('Вася')
print(name)
