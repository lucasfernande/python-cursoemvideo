def moeda(p = 0, moeda = 'R$'):
    return f'{moeda} {p:>.2f}'.replace('.', ',')

def metade(p = 0, formatar = False):
    return p / 2 if formatar is False else moeda(p / 2)

def dobro(p = 0, formatar = False):
    return p * 2 if formatar is False else moeda(p * 2)

def reajuste(tipo, p = 0, taxa = 0, formatar = False):
    if tipo not in '+-':
        return None
    else:
        if tipo == '+':
            p = p + (p * taxa / 100)
        else:
            p = p - (p * taxa / 100)
    
    return p if formatar is False else moeda(p)
