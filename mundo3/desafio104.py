def leiaInt(msg):
    while True:
        n = input(msg)

        if n.isdigit():
            break
        else:
            print('\033[31m', 'Erro! Digite um número inteiro válido', '\033[0;0m', sep='')
    
    return int(n)

n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')