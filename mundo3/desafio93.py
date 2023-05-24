jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou?: '))

for i in range(jogos):
    v = int(input(f'Quantos gols fez na {i + 1}° partida: '))
    gols.append(v)

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('~' * 40)

for k, v in jogador.items():
    print(f'{k} -> {v}')

print('~' * 40)

print(f'O jogador {jogador["nome"]} jogou {jogos} partidas')
for i, x in enumerate(jogador['gols']):
    print(f'{"=>":>5} Na {i + 1}° partida, fez {x} gols')

print(f'{jogador["nome"]} fez um total de {jogador["total"]} gols')