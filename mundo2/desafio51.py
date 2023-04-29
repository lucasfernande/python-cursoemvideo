a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

print('PA:')
for i in range(1, 11):
    print(f'{a}', end=' => ')
    a += r

print('Fim')