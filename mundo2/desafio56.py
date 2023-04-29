somaIdades = 0
mulherMenos20 = 0

for i in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ')

    somaIdades += idade

    if i == 0:
        nomeHomemMaisVelho = nome
        maiorIdade = idade

    if sexo == 'M' and idade > maiorIdade:
        nomeHomemMaisVelho = nome
        maiorIdade = idade

    if sexo == 'F' and idade < 20:
        mulherMenos20 += 1

print(f'A média de idade foi {somaIdades / 4:.2f} anos')
print(f'O homem mais velho foi o {nomeHomemMaisVelho}, com {maiorIdade} anos')
print(f'{mulherMenos20} mulheres com menos de 20 anos')