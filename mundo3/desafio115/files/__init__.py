def criar(nome):
    try:
        arq = open(nome, 'x')
        arq.close()
    except FileExistsError:
        return
    
def cadastrar(nome, idade):
    with open('registros.txt', 'a', encoding='utf-8') as r:
        r.write(f'{nome} {idade}\n')
    