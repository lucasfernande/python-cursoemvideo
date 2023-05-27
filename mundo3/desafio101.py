from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano

    if idade >= 18 and idade <= 65:
        voto = 'Obrigatório'
    elif idade >= 16:
        voto = 'Opcional'
    else:
        voto = 'Negado'
    
    return f'Com {idade} anos: {voto}'
    
ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))