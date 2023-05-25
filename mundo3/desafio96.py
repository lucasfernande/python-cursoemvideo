def msg(m):
    print(m.center(30))
    print('-' * 30)

def area(b, h):
    print(f'A área de um terreno {b} x {h} é {b * h}m²')


msg('Área do Terreno')

b = float(input('Largura: '))
h = float(input('Comprimento: '))
area(b, h)
