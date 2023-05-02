cont = 0
soma = 0

while True:
    n = int(input('Digite um número (999 para encerrar o programa): '))

    if n == 999:
        break
    else:
        cont += 1
        soma += n

print(f'Você digitou {cont} números, e a soma deles foi {soma}')