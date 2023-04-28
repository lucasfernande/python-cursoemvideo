preco = float(input('Digite o preço do produto: '))
forma = input('Digite a forma de pagamento (Dinheiro/<número>x): ')

if forma == 'Dinheiro':
    print(f'Ganhou 10% de desconto! O novo valor é: R$ {preco * 0.9}')
elif forma == '1x':
    print(f'Ganhou 5% de desconto! O novo valor é: R$ {preco * 0.95}')
elif forma == '2x':
    print('Sem desconto')
else:
    print(f'Juros de 20%. O novo valor é: {preco * 1.20}')