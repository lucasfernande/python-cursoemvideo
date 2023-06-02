def leiaInt(msg):
    while True:
        n = input(msg).strip()
        try:
            n = int(n)
        except (ValueError, TypeError):
            if n == '':
                return 0
            else:
                print('\033[0;31mERRO: digite um número inteiro válido\033[0m')
                continue
        except KeyboardInterrupt:
            print('Programa encerrado')
            return 0
        else:
            return n
        
def leiaFloat(msg):
    while True:
        n = input(msg).strip()
        try:
            n = float(n)
        except (ValueError, TypeError):
            if n == '':
                return 0
            else:
                print('\033[0;31mERRO: digite um número real válido\033[0m')
                continue
        except KeyboardInterrupt:
            print('Programa encerrado')
            return 0
        else:
            return n

i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'O número inteiro foi {i}, e o real foi {f}')