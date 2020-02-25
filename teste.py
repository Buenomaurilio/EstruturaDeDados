import exerciciosEstruturaDeDados
from exerciciosEstruturaDeDados import returnLista
from random import*

""" def buscaBinaria(lista,n):
    esq = 0
    dir = len(lista)-1
    if esq <= dir:
        meio = (esq + dir)//2
        if lista[meio] == n:
            return print(f'achou no indice central {meio}, valor {lista[meio]}')
        elif n <= lista[meio]:
            dir = meio -1
        else:
            esq =  meio +1
    return print('não encontrou')

aleatorio = randrange(1,30)
n = 3 #randrange(10,110)
print(n)
lista = returnLista(n)
print(lista)
localizacao = buscaBinaria(lista,aleatorio)                    
  """


 
#import exercicios_japeruano
from random import randrange
import exerciciosEstruturaDeDados
from exerciciosEstruturaDeDados import returnLista


def buscabinaria(lista,numero):
    #lista.sort()
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2 

        if lista[meio] == numero:
            return print(f"Achou no indice {meio}, valor {lista[meio]}")
        
        elif numero <= lista[meio]:
            direita = meio - 1
        
        else:
            esquerda = meio + 1
                
    return print('nao encontrou') 

aleatorio = randrange(0, 30)
print(f'numero aleatorio: {aleatorio}') 
numero = randrange(-30, 30)
print(f'range da lista: {numero}') 
#print(numero)
lista = returnLista(numero)
print(lista)
localizacao = buscabinaria(lista, aleatorio)

# 1) Dado um número N definido por você, criar uma lista de tamanho N\
#formada por números aleatórios com valores entre –N e N.\
#Exemplo: N = 5\
#Lista = [-3, 4, 0, 2, -1]
































