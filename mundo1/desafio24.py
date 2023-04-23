cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(f'Começa com Santo?: {cidade.upper()[0:5] == "SANTO"}')