tabela = ('PAL', 'BOT', 'FLU', 'CAP', 'CRU', 'FOR', 'SAO', 'CAM', 'SAN', 'GRE', 'INT', 'FLA', 'BAH', 'BGT', 'VAS', 'COR', 'CUI', 'GOI', 'AME', 'CFB')

print('Os cinco primeiros colocados são: ')
for i in range(5):
    print(f'{i + 1}° - {tabela[i]}')

print('~' * 30)

print('Os quatro últimos colocados são: ')
for i in range(16, 20):
    print(f'{i + 1}° - {tabela[i]}')

print('~' * 30)

print('Times em ordem alfabética: ')
print(sorted(tabela))

print('~' * 30)

print(f'O Vasco está na {tabela.index("VAS") + 1}° posição')