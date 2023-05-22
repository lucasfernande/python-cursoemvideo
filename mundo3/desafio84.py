pessoas = list()

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))

    if len(pessoas) == 0:
        maiorPeso = menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        
        if peso < menorPeso:
            menorPeso = peso

    pessoas.append([nome, peso])

    continuar = str(input('Deseja continuar?: [S/N]: '))[0]
    if continuar in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso foi {maiorPeso} kg, cadastrado para', end=' ')
for p in pessoas:
    if p[1] == maiorPeso:
        print(p[0], end=' ')

print()

print(f'O menor peso foi {menorPeso} kg, cadastrado para', end=' ')
for p in pessoas:
    if p[1] == menorPeso:
        print(p[0], end=' ')