from time import sleep

cores = {
    'padrao': '\033[m',
    'vermelho': '\033[0;30;41m',
    'roxo': '\033[0;30;45m',
    'verde': '\033[0;30;42m',
    'branco': '\033[7;30m'
}

def titulo(msg, cor='padrao'):
    caracteres = len(msg) + 4
    print(cores[cor])
    print('-' * caracteres)
    print(msg.center(caracteres))
    print('-' * caracteres)
    print(cores['padrao'])


def manual(c):
    titulo(f'Acessando o manual do comando {c}', 'roxo')
    print(cores['verde'])
    help(c)
    print(cores['padrao'])

titulo('Sistema de Ajuda PyHelp', 'verde')

while True:
    comando = str(input('Função ou biblioteca > '))

    if comando.lower() in 'sair':
        break

    manual(comando)

titulo('FIM', 'vermelho')