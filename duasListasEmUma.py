from random import*
import math

def returnLista(namber):
    lista = []
    for i in range(namber):
        a = randrange(-namber, namber)
        lista.append(a)
    print(f'Verifica evolucao lista interna: {lista}')    
    return lista



def duas_em_uma():
    N = int(input('Enter the number: '))

    a = randrange(0, N-1)
    b = randrange(0, N-1)

    listaa = returnLista(a)
    listab = returnLista(b)
    listac = []
    
    for i in listaa:
        listac.append(i)
    for i in listab:
        listac.append(i)
    listac.sort()    
    return listac


x = duas_em_uma()
print(x)            
 
'''
5) Dado um número aleatório a, criar uma função de busca linear que\
procure a na lista criada na pergunta 1. A função criada deve retornar o\
índice no qual o elemento buscado está armazenado na lista ou um indicador caso não se encontre.
'''


""" namber = int(input('Enter the number: '))
a = randrange(-namber, namber)
c = returnLista(namber)  


def inlista(lista, a):
    for i in lista:
        if lista[i] == a:
            return i
        else:
            return False


#n = int(input('Enter the number: '))
              
x = inlista(c, a)
print(x) """


""" 
6) Dado um número aleatório a, criar uma função de busca binária que
procure a na lista criada na pergunta 1. A função criada deve retornar o
índice no qual o elemento buscado se encontra na lista ou um indicador
caso não se encontre.
 """
 