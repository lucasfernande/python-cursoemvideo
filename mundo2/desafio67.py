while True:
    n = int(input('Digite um número para a tabuada (negativo para encerrar): '))

    if n < 0:
        break

    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('~' * 20)

print('Fim')