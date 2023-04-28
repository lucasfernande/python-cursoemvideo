n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Reprovado! :(')
elif media < 7:
    print('Em recuperação')
else:
    print('Aprovado! :)')