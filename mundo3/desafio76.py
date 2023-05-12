produtos = ('Feijão', 8.00, 'Arroz', 16.00, 'Carne', 25.00)

print('~' * 40)
print('Catálogo de Produtos'.center(40))
print('~' * 40)

for i, item in enumerate(produtos):
    if i % 2 == 0:
        print(f'{item:.<30}', end='')
    else:
        print(f'R$ {item:>5.2f}')
print('~' * 40)