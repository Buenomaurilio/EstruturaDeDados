from random import randrange

def lista(number):
    list = []
    for i in range(number):
        x = randrange(-number, number)
        list.append(x)
        print(f'list: {list}')
    return list

number = int (input('number: '))
x = randrange(-number, number)
print(f'list{x}')
print(lista(number))
