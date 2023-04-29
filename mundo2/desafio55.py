maior = 0
menor = 0

for i in range(5):
    peso = float(input('Digite o peso: '))
    if i == 0:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso


print(f'O maior peso digitado foi: {maior} kg')
print(f'O menor peso digitado foi: {menor} kg')
    