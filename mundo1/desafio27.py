nome = str(input('Digite seu nome completo: ')).strip()

print(f'O primeiro nome é {nome.split()[0]}')
print(f'O último nome é {nome.split()[-1]}')