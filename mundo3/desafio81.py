valores = list()

while True:
    v = int(input('Digite um valor (-1 para parar): '))

    if v < 0:
        break
    else:
        valores.append(v)

print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Valores em ordem decrescente: {valores}')

if 5 in valores:
    print(f'Você digitou o valor 5!')
else:
    print('Você não digitou o valor 5!')