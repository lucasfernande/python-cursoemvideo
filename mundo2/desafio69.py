contMaior = contMasc = contFem20 = 0

print('~' * 30)
print('CADASTRO'.center(30))
print('~' * 30)

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [M/F]: '))
    
    if idade >= 18:
        contMaior += 1

    if sexo in 'Mm':
        contMasc += 1

    if sexo in 'Ff' and idade < 20:
        contFem20 += 1

    continuar = ' '
    while continuar not in 'SsNn': 
        continuar = str(input('Cadastrar outra pessoa? [S/N]: '))
    
    if continuar in 'Nn':
        break

    print('~' * 30)

print('~' * 30)
print(f'Foram registradas {contMaior} pessoas maiores de idade')
print(f'Foram registradas {contMasc} pessoas do sexo masculino')
print(f'Foram registradas {contFem20} pessoas do sexo feminino com menos de 20 anos')