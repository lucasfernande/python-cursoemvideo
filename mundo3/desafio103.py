def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

jog = input('Nome do jogador: ')
gol = input('Número de gols: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jog.strip() == '':
    ficha(gol=gol)
else:
    ficha(jog, gol)