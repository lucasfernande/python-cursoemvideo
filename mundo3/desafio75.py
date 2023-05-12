lista = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
)

print('~' * 30)
print(f'Você digitou os valores {lista}')

print(f'O valor 9 apareceu {lista.count(9)} vezes')

if 3 in lista:
    print(f'O valor 3 foi digitado na {lista.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')

print('Os valores pares digitados foram: ', end='')
for item in lista:
    if item % 2 == 0:
        print(item, end=' ')