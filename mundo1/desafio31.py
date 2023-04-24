km = int(input('Digite a distância da viagem: '))

if km < 200:
    print(f'O valor a pagar é de: R$ {0.5 * km}')
else: 
    print(f'O valor a pagar é de: R$ {0.45 * km}')