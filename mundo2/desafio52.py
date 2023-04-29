n = int(input('Digite um número: '))
vezesDiv = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(f'\033[32m {i}', end='')
        vezesDiv += 1
    else:
        print(f'\033[31m {i}', end='')

print(f'\nO número {n} foi divisível {vezesDiv} vezes')

if vezesDiv == 2: # apenas por 1 e por ele mesmo
    print(f'{n} é um número primo!')
else:
    print(f'{n} não é primo!')