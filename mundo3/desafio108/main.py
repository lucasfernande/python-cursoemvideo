import moeda

p = float(input('Digite o preço: R$ '))

pFormatado = moeda.moeda(p)

print(f'A metade de R$ {pFormatado} é: {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R$ {pFormatado} é: {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%: {moeda.moeda(moeda.reajuste("+", p, 10))}')
print(f'Reduzindo 13%: {moeda.moeda(moeda.reajuste("-", p, 13))}')