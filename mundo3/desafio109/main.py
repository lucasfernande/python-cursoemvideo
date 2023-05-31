import moeda

p = float(input('Digite o preço: R$ '))

pFormatado = moeda.moeda(p)

print(f'A metade de R$ {pFormatado} é: {moeda.metade(p, True)}')
print(f'O dobro de R$ {pFormatado} é: {moeda.dobro(p, True)}')
print(f'Aumentando 10%: {moeda.reajuste("+", p, 10, True)}')
print(f'Reduzindo 13%: {moeda.reajuste("-", p, 13, True)}')