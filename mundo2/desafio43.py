altura = float(input('Digite sua altura (Ex: 1.80): '))
peso = float(input('Digite seu peso: '))

imc = peso / altura ** 2
print(f'Seu imc é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')