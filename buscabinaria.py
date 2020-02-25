""" import time

def busca_binaria(lista,p,fi,n):
    if p <= fi:
        m = (p + fi)//2
        if n > lista[m]:
            return busca_binaria(lista, m + 1,fi,n)
        elif n < lista[m]:
            return busca_binaria(lista,p,m - 1, n)
        else:
            return m

    return -1   


lista = list(range(1, 10000000))

chave = 9999999
antes = time.time()
posicao = busca_binaria(lista, 0, len(lista)-1,chave)
depois = time.time()
total = (depois - antes)*1000
if posicao >= 0:
    print('o elemento %d foi encontrado em %d.'%(chave, posicao))
else:
    print('o elemento %d Não foi encontrado.'% chave)
#print(lista)              
print('o tempo total gasto foi:  %0.2f ms'% total)


vetor = list(range(0, 10))

print(vetor)  """

from random import*
import time

lista = []

for i in range(1000000):
    a = randrange(0, 100)
    lista.append(a)
antes = time.time()    
print(len(lista))
depois = time.time()
total = (depois - antes)*1000
print('ms',total)