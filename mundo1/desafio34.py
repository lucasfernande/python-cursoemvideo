salario = float(input('Digite o seu salário: '))

if salario > 1250:
    print(f'Você recebeu um aumento de 10%, seu novo salário é: R$ {salario * 1.10:.2f}')
else:
    print(f'Você recebeu um aumento de 15%, seu novo salário é: R$ {salario * 1.15:.2f}')