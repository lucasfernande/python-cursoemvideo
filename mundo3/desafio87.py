matriz = [[], [], []]
somaPares = 0
somaTerceiraColuna = 0

for l in range(3):
    for c in range(3):
        v = int(input(f'Digite o valor para ({l}, {c}): '))
        matriz[l].append(v)

        if v % 2 == 0:
            somaPares += v

print('~' * 50)

for linha in matriz:
    somaTerceiraColuna += linha[2]
    for item in linha:
        print(f'[ {item} ]', end=' ')
    print()

print('~' * 50)
print(f'A soma dos valores pares foi: {somaPares}')
print(f'A soma dos valores da 3° coluna foi: {somaTerceiraColuna}')

for i, v in enumerate(matriz[1]):
    if i == 0:
        maior = v
    
    if v > maior:
        maior = v

print(f'O maior valor da segunda linha é: {maior}')