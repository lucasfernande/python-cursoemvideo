from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # itemgetter(1) -> ordena pelo "indice" 1 (número do dado)
for i, v in enumerate(ranking):
    print(f'{i + 1}° Lugar - {v[0]} -> {v[1]}')