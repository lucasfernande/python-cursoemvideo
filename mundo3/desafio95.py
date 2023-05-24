jogadores = list()

while True:
    jogador = dict()
    gols = list()

    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou?: '))

    for i in range(jogos):
        v = int(input(f'Quantos gols fez na {i + 1}° partida: '))
        gols.append(v)

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador)

    while True:
        c = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if c in 'SN':
            break
        print('ERRO: digite apenas S ou N')
    
    if c in 'N':
        break

print('~' * 40)

print(f'{"cód":<5}', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()

print('-' * 40)
for i, v in enumerate(jogadores):
    print(f'{i:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Digite o código do jogador: '))

    if busca == 999:
        break

    if busca < 0 or busca >= len(jogadores):
        print(f'ERRO: não existe jogador com o código {busca}')
    else:
        print(f'Estatísticas do jogador {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'Na {i + 1}° partida, fez {g} gols')
    print('~' * 40)