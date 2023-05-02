n = int(input('Digite um número inteiro para calcular o fatorial: '))
c = n
fatorial = 1

while c > 0:
    print(f'{c}', 'x ' if c > 1 else '= ', end='')
    fatorial *= c
    c -= 1

print(fatorial)