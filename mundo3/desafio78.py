valores = list()

for i in range(5):
    n = int(input(f'Digite um número para a {i}° posição: '))
    valores.append(n)

maior = max(valores)
menor = min(valores)

print(f'Você digitou os valores: {valores}')

print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=' ')

print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=' ')

