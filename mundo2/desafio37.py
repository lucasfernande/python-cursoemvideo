n = int(input('Digite um número: '))
base = int(input('Digite para qual você quer convertê-lo\n(2 - Binário, 8 - Octal, 16 - Hexadecimal): '))
resp = ''
decimal = n

if base == 2:
    while n != 0:
        resto = n % 2
        resp = str(resto) + resp
        n = n // 2
    print(f'{decimal} em base {base} é: {resp}')
elif base == 8:
    while n != 0:
        resto = n % 8
        resp = str(resto) + resp
        n = n // 8
    print(f'{decimal} em base {base} é: {resp}')
elif base == 16:
    while n != 0:
        resto = n % 16

        if resto == 10:
            resto = 'A'
        if resto == 11:
            resto = 'B'
        if resto == 12:
            resto = 'C'
        if resto == 13:
            resto = 'D'
        if resto == 14:
            resto = 'E'
        if resto == 15:
            resto = 'F'

        resp = str(resto) + resp
        n = n // 16
    print(f'{decimal} em base {base} é: {resp}')
else:
    print('Valor inválido')

