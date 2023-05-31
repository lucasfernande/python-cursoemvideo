def moeda(p = 0, moeda = 'R$'):
    return f'{moeda} {p:>.2f}'.replace('.', ',')

def metade(p = 0):
    return p / 2

def dobro(p = 0):
    return p * 2

def reajuste(tipo, p = 0, taxa = 0):
    if tipo not in '+-':
        return None
    else:
        if tipo == '+':
            return p * (1 + taxa / 100)
        else:
            return p * (1 - taxa / 100)
