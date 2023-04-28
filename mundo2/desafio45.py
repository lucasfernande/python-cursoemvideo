from random import choice

maquina = ['Pedra', 'Papel', 'Tesoura']

while True:
    minhaJogada = input('Digite sua jogada (Pedra/Papel/Tesoura): ')
    jogadaMaquina = choice(maquina)
    if not minhaJogada:
        break
    else: 
        if (minhaJogada == 'Pedra' and jogadaMaquina == 'Tesoura') or (minhaJogada == 'Papel' and jogadaMaquina == 'Pedra') or (minhaJogada == 'Tesoura' and jogadaMaquina == 'Papel'):
            print(f'\nVocê escolheu {minhaJogada} e a máquina escolheu {jogadaMaquina}. Você VENCEU!')
        elif (jogadaMaquina == 'Pedra' and minhaJogada == 'Tesoura') or (jogadaMaquina == 'Papel' and minhaJogada == 'Pedra') or (jogadaMaquina == 'Tesoura' and minhaJogada == 'Papel'):
            print(f'\nA máquina escolheu {jogadaMaquina} e você escolheu {minhaJogada}. A máquina VENCEU!')
        else:
            print(f'\nA máquina escolheu {jogadaMaquina} e você escolheu {minhaJogada}. EMPATE!')
