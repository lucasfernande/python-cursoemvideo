from math import hypot

op = float(input('Digite o cateto oposto: '))
ad = float(input('Digite o cateto adjacente: '))
hip = hypot(op, ad)

print(f'A hipotenusa é: {hip}')