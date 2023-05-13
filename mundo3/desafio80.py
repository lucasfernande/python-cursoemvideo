lista = list()

for i in range(5):
    n = int(input('Digite um valor: '))

    if i == 0 or n >= lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        for pos, v in enumerate(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break

print(f'Os valores em ordem foram: {lista}')