ano = int(input('Digite seu ano de nascimento: '))
idade = 2023 - ano

if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade < 18:
    print(f'Ainda falta {18 - idade} anos para você se alistar! {2023 + (18 - idade)}')
else:
    print(f'Já passou {idade - 18} anos do seu tempo de alistamento! {2023 - (idade - 18)}')