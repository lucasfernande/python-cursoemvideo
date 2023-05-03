total = mais1000 = contador = precoBarato = 0
nomeBarato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: '))
    contador += 1
    total += preco

    if contador == 1 or preco < precoBarato:
        nomeBarato = produto
        precoBarato = preco
     
    if preco > 1000.0:
        mais1000 += 1

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: '))
    
    print('~' * 30)

    if continuar in 'Nn':
        break

print(f'Valor total da compra: R$ {total:,.2f}')
print(f'Foram comprados {mais1000} produtos com preço maior que R$ 1000')
print(f'O produto mais barato foi {nomeBarato}, custando R$ {precoBarato:,.2f}')