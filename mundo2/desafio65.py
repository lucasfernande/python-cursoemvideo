resp = 'S'
maior = 0
menor = 10000000000000000000000000000000000000000000
soma = 0
cont = 0


while resp in 'Ss':
    n = float(input('Digite um número: '))
    cont += 1
    soma += n

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    resp = str(input('Deseja adicionar outro número?: '))

print(f'A média entre os valores digitados foi de: {soma / cont}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')