a = float(input('Digite o 1° número: '))
b = float(input('Digite o 2° número: '))

while True:
    print('\nO que você quer fazer com esses números?', '[ 1 ] Somar', '[ 2 ] Multiplicar', '[ 3 ] Qual o maior?', '[ 4 ] Novos números', '[ 5 ] Sair do programa', sep='\n')
    opcao = input('Digite sua opção: ')

    if opcao == '1':
        print(f'{a} + {b} = {a + b}')
    if opcao == '2':
        print(f'{a} x {b} = {a * b}')
    if opcao == '3':
        if a > b:
            print(f'{a} é maior que {b}')
        elif b > a:
            print(f'{b} é maior que {a}')
        else:
            print('Os valores são iguais')
    if opcao == '4':
        a = float(input('Digite o 1° número: '))
        b = float(input('Digite o 2° número: '))
    if opcao == '5':
        break

print('Programa encerrado')