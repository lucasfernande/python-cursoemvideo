valores = list()

while True:
    v = int(input('Digite um valor (-1 para parar): '))

    if v < 0:
        break
    else:
        valores.append(v)

pares = list()
impares = list()

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

pares.sort()
impares.sort()

print(f'Você digitou os valores: {valores}')
print(f'Os valores PARES que você digitou foram: {pares}')
print(f'Os valores ÍMPARES que você digitou foram: {impares}')