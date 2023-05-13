valores = list()

while True:
    v = int(input('Digite um valor (-1 para parar): '))

    if v == -1:
        print('~' * 30)
        break
    else:
        if v in valores:
            print(f'Esse valor já existe')
        else:
            valores.append(v)
            print('Valor adicionado!')

valores.sort()
print(f'Valores digitados em ordem crescente: {valores}')