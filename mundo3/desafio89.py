boletins = list()

while True:
    nome = str(input('Digite o nome: '))
    n1 = float(input('Digite a 1° nota: '))
    n2 = float(input('Digite a 2° nota: '))

    boletins.append([nome, [n1, n2]])

    continuar = str(input('Deseja continuar? [S/N]: '))[0]
    if continuar in 'Nn':
        print('~' * 40)
        break

print(f'{"N°":<5} {"Nome":<10} {"Média":<10}')

for i, p in enumerate(boletins):
    media = (p[1][0] + p[1][1]) / 2
    print(f'{i:<5} {p[0]:<10} {media:<10.2f}')

print('~' * 40)

while True:
    opc = int(input('Quer mostrar as notas de qual aluno? (999 para parar): '))

    if opc == 999:
        break
    
    if opc in range(len(boletins) - 1):
        nome = boletins[opc][0]
        notas = boletins[opc][1]
        print(f'Notas do aluno(a) {nome}: {notas}')
    else:
        print('Número de aluno inválido')
        