'''
1) Dado um número N definido por você, criar uma lista de tamanho N formada por números aleatórios com valores entre –N e N. 
Exemplo: N = 5\
Lista = [-3, 4, 0, 2, -1]
'''
from random import randrange
import math

def returnLista(namber):
    lista = []
    for i in range(namber):
        a = randrange(-namber, namber)
        lista.append(a)
    print(f'Verifica evolucao lista interna: {lista}')    
    return lista

""" 
2) Calcular o valor médio da lista criada na pergunta 1.\
Exemplo:  Médio = -3 + 4 + 0 + 2 – 1 = 2 """


""" def media(lista):
    soma = 0
    media = 0
    tam = len(lista)
    for i in range(tam):
        soma += lista[i]
    media = soma/tam
    return media

n = int(input('Enter the number:  '))

x = returnLista(n)
b = media(x)
print(f'Media: {b}')
 """



""" 3) Dado um número aleatório a, o qual pode tomar valores entre 0 e N-1, e \
dada a lista criada na pergunta 1, criar uma função que retorne duas (sub)\
listas a partir dessa lista inicial.\
A primeira (sub) lista chamada esquerda, deverá conter os valores da lista inicial que estão\
armazenados nos índices menores ao valor de a,\
enquanto que a segunda (sub) lista, chamada direita, deverá conter os valores da lista inicial\
armazenados nos índices maiores ou iguais ao valor de a.\
Exemplo:\
a = 2\
esquerda = [-3, 4]\
direita = [0, 2, -1]
 """

def dividelista(lista, alA):
    esquerda = []
    direita = []
    tam = len(lista)
    for i in range(tam):
        if lista[i] < alA:
            esquerda.append(lista[i])
        else:
            direita.append(lista[i])
    return esquerda, direita

n = -1
while n < 0:
    n = int(input('Enter the number more than 0: '))

x = returnLista(n)
a = randrange(0, (n-1))
print(f'Valor de A: {a}')
j = dividelista(x, a)
print(j)    




