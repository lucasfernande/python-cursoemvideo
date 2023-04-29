print('Números pares entre 1 e 50:')

for i in range(2, 51, 2): # não é necessário executar o laço nos números ímpares, então podemos pular de 2 em 2
    if i % 2 == 0:
        print(i, end=' ')