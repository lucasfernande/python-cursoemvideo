r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem formar um triângulo!')

    if r1 == r2 == r3:
        print('Elas formarão um triângulo equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Elas formarão um triângulo isósceles!')
    else:
        print('Elas formarão um triângulo escaleno!')
else:
    print('As retas não podem formar um triângulo.')