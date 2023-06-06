def menu():
    print('~' * 50)
    print('Menu Principal'.upper().center(50))
    print('~' * 50)

    print(f'1 - Ver pessoas cadastradas')
    print(f'2 - Cadastrar nova pessoa')
    print(f'3 - Sair')
    print('~' * 50)

def registros():
    with open('registros.txt', 'r', encoding='utf-8') as r:
        pessoas = r.readlines()

    print(f'{"Nome":<25}{"Idade"}')
    print('-' * 32)
    
    for p in pessoas:
        espaco = p.rfind(' ') # pegando o espaço antes da idade, para separar nome e idade

        nome = p[:espaco]
        idade = p[espaco + 1:].replace('\n', '')

        print(f'{nome:<25}{idade} anos')