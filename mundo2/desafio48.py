print('Números ímpares que são múltiplos de 3 entre 1 e 500: ')
soma = 0
cont = 0

for i in range(1, 501, 2): # # não é preciso executar o laço nos números pares, então podemos pular de 2 em 2
    if i % 2 != 0 and i % 3 == 0:
        print(i, end=' ')
        cont += 1
        soma += i

print(f'\nExistem {cont} valores ímpares e múltiplos de 3 entre 1 e 500')
print(f'A soma de todos esses números é: {soma}')