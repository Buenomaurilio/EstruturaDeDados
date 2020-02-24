'''
implementar uma função troca, que recebe uma lista e duas posições, e troca os valores da duas posições.

exemplo:
    troca(['a','b','c'],0,1) deve retornar ['b','a','c']
outro exemplo:
    troca(['a','b','c'],0,2) deve retornar ['c','b','a']
'''

def troca (lista,a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux
    
    return lista
#lista = [7,5,3,8,2]

#print(troca(lista,0,3))

'''
implemente uma função indice_menor,que recebe uma lista e devolve o indice do seu menor elemento.
se houver mais de um menor elemento, retorna
'''



def indice_menor(lista):
    menor = lista[0]
    indice = 0
    for valor in lista:
        if valor < menor:
           menor = valor
           indice = lista.index(valor)
    return indice         



#lista = [4,5,0,9,7,6,3,1,8,0]
#print(indice_menor(lista))

'''
monte uma função quebra_em_dois que recebe uma lista l e um numero D.
que devolve duas listas: uma com numeros de L menor que D e outra com números maiores que D
se L tiver algum numero igual ele deve ser 

'''
def quebra_em_dois(lista, D):
    maiores = []
    menores = []    
    for i in range(len(lista)):
        if lista[i] >= D:
            maiores.append(lista[i])
        else:
            menores.append(lista[i])    
    return maiores, menores

lista = [7,5,8,3,6,2,9]
print(quebra_em_dois(lista, 6))





