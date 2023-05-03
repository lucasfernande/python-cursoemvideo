valor = float(input('Digite o valor do saque: R$ '))
print('~' * 30)
total = valor
cedulaAtual = 50 # 50, 20, 10 e 1
cedulas = 0

while True:
    if total >= cedulaAtual:
        total -= cedulaAtual
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'{cedulas} cédulas de R$ {cedulaAtual}')
        cedulas = 0
        if cedulaAtual == 50:
            cedulaAtual = 20
        elif cedulaAtual == 20:
            cedulaAtual = 10
        elif cedulaAtual == 10:
            cedulaAtual = 1

        if total == 0:
            print('~' * 30)
            break

print('Obrigado e volte sempre!')

