a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

t = 1
while t <= 10:
    print(f'{a}', end=' => ')
    a += r
    t += 1

t = int(input('\nDeseja mostrar mais quantos termos? (0 para encerrar): '))
cont = 1
while cont <= t:
    print(f'{a}', end=' => ')
    a += r
    cont += 1

print('Fim')