pessoas = list()
somaIdades = 0

while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()[0]
        if sexo in 'MF':
            break
        print('ERRO: digite apenas M ou F')

    idade = int(input('Idade: '))

    somaIdades += idade

    pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})

    while True:
        c = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if c in 'SN':
            break
        print('ERRO: digite apenas S ou N')
    
    if c in 'N':
        break
            

qtdPessoas = len(pessoas)
mediaIdade = somaIdades / qtdPessoas

print(f'O grupo tem {qtdPessoas} pessoas.')
print(f'A média de idade do grupo é {mediaIdade:.2f}.')

print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(p['nome'], end=' ')

print()

print('Pessoas com idade acima da média: ')
for p in pessoas:
    if p['idade'] > mediaIdade:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} -> {v};', end=' ')