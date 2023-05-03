from random import randint

venceu = 0

while True:
    jogada = int(input('Digite um valor: '))
    pc = randint(0, 10)

    parOuImpar = ' '
    while parOuImpar not in 'PpIi':
        parOuImpar = str(input('Par ou Ímpar? [P/I]: '))

    if parOuImpar in 'Pp':
        if (jogada + pc) % 2 == 0:
            print(f'Você jogou {jogada} e a máquina {pc} = {jogada + pc}, PAR') 
            print('Você GANHOU!')
            print('~' * 30)
            venceu += 1
        else:
            print(f'Você jogou {jogada} e a máquina {pc} = {jogada + pc}, ÍMPAR')
            print('Você PERDEU!') 
            print('~' * 30)
            break
    else:
        if (jogada + pc) % 2 != 0:
            print(f'Você jogou {jogada} e a máquina {pc} = {jogada + pc}, ÍMPAR') 
            print('Você GANHOU!')
            print('~' * 30)
            venceu += 1
        else:
            print(f'Você jogou {jogada} e a máquina {pc} = {jogada + pc}, PAR')
            print('Você PERDEU!') 
            print('~' * 30)
            break

print(f'Game Over! Você venceu {venceu} vezes!')