ns = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True: 
    num = int(input('Digite um número de 0 a 20: '))
    while num not in range(0, 21):
        num = int(input('Digite um número de 0 a 20: '))

    print(f'Você digitou o número {ns[num]}')

    cont = str(input('Quer digitar outro número? [ S/N ]: '))
    while cont not in 'SsNn':
        cont = str(input('Quer digitar outro número? [ S/N ]: '))

    if cont in 'Nn':
        break

print('Fim')