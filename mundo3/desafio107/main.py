import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de R$ {p} é: {moeda.metade(p)}')
print(f'O dobro de R$ {p} é: {moeda.dobro(p)}')
print(f'Aumentando 10%: {moeda.reajuste("+", p, 10)}')
print(f'Reduzindo 13%: {moeda.reajuste("-", p, 13)}')