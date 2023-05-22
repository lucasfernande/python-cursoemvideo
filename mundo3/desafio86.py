matriz = [[], [], []]

for l in range(3):
    for c in range(3):
        v = int(input(f'Digite o valor para ({l}, {c}): '))
        matriz[l].append(v)

print('~' * 50)
for linha in matriz:
    for item in linha:
        print(f'[ {item} ]', end=' ')
    print()