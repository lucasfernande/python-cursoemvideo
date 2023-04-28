a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

if a > b:
    print(f'O primeiro valor ({a}) é maior que o segundo ({b})')
elif b > a:
    print(f'O segundo valor ({b}) é maior que o primeiro ({a})')
else:
    print(f'Os dois valores são iguais!')