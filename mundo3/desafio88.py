from time import sleep
from random import randint

print('~' * 40)
print('JOGA NA MEGA SENA'.center(40))
print('~' * 40)

qtdJogos = int(input('Quantos jogos você quer sortear?: '))

for i in range(qtdJogos):
    jogo = list()
    for x in range(6):
        v = randint(1, 60)

        while True:
            if v in jogo:
                v = randint(1, 60)
            else:
                break
            
        jogo.append(v)
        jogo.sort()

    sleep(1)
    print(f'Jogo {i + 1}: {jogo}')

print(f'Boa sorte!')
