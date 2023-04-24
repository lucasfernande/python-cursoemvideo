km = int(input('Digite quantos km/h estava o carro: '))

if km > 80:
    print(f'Você foi multado! Sua multa será de R$ {(km - 80) * 7}')
else:
    print('Você não foi multado.')