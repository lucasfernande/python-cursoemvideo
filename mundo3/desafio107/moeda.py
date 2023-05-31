def metade(p):
    return p / 2

def dobro(p):
    return p * 2

def reajuste(tipo, p, taxa):
    if tipo not in '+-':
        return None
    else:
        if tipo == '+':
            return p * (1 + taxa / 100)
        else:
            return p * (1 - taxa / 100)
