a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while t <= total:
        print(f'{a}', end=' => ')
        a += r
        t += 1
    print('PAUSA')
    mais = int(input('\nVocê deseja mostrar mais quantos termos?: '))
print('FIM') 

print(f'Foram mostrados {total} termos')
