a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite mais um número: '))

if a > b and a > c:
    print(f'{a} é o maior número')
elif b > a and b > c:
    print(f'{b} é o maior número')
else:
    print(f'{c} é o maior número')

if a < b and a < c:
    print(f'{a} é o menor número')
elif b < a and b < c:
    print(f'{b} é o menor número')
else:
    print(f'{c} é o menor número')