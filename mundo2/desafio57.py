s = str(input('Digite seu sexo (M/F): ')).strip().upper()[0]

while s not in 'MmFf':
    s = str(input('Pelo amor de Deus, digite M ou F: ')).strip().upper()[0]

print(f'Sexo {s} registrado.')