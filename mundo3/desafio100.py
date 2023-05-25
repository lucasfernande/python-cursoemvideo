from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores: ', end='')
    for i in range(5):
        v = randint(1, 10)
        print(v, end=' ')
        lista.append(v)
        sleep(0.5)
    print()

def pares(lista):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    
    print(f'A soma dos pares de {lista} é {soma}')
        

lista = list()
sorteia(lista)
pares(lista)
