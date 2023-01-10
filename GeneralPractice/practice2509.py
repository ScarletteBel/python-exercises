
def bag():
    bag1 = "456"

    return bag1

answer = bag()
print(type(answer))
print(type(bag()))
print(type(bag))
print()
print('answer: ', answer) 
print('I am printing bag() ',bag())
rci = bag
print('Printing bag: ', bag)
print('Printing rci: ', rci)
print('Printing rci(): ', rci())


def gretting():
    global message 
    message = "Hola mundo"
    print(message)

gretting()

print(message)

y = "Viva Mexico"
def country():
    x = "I like quesadillas con queso"
    print(f'I am saying: {x} {y}')

country()

def name():
    lastName = "ito"
    name  = "Andres ya cogeme"
    return (lastName, name)

def name1():
    lastName = "ito"
    name  = "Andres ya cogeme"
    return lastName, name 

print(type(name()))
print(type(name1()))




