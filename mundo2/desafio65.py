resp = 'S'
soma = cont = maior = menor = 0

while resp in 'Ss':
    n = float(input('Digite um número: '))
    cont += 1
    soma += n

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        
    resp = str(input('Deseja adicionar outro número?: '))

print(f'A média entre os valores digitados foi de: {soma / cont}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')