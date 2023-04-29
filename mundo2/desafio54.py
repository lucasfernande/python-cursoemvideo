from datetime import date
atual = date.today().year

maior = 0
menor = 0

for i in range(7):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = atual - nasc

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas são maiores de idade, e {menor} são menores de idade')