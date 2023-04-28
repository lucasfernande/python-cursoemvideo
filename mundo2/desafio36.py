casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
meses = int(input('Digite em quantos anos será pago: '))
meses *= 12

prestacao = casa / meses
print(f'Você pagará RS {casa:,.2f} em {meses} parcelas de R$ {prestacao:,.2f}')

if prestacao >= (salario * 0.3):
    print('O empréstimo não pode ser aprovado :(')
else:
    print(f'Empréstimo aprovado!')
