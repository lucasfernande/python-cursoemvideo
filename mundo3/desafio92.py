from datetime import date
anoAtual = date.today().year

dados = dict()

dados['nome'] = str(input('Digite o nome: '))
anoNasc = int(input('Digite o ano de nascimento: '))
dados['idade'] = anoAtual - anoNasc
dados['ctps'] = int(input('Digite o n° da carteira de trabalho: '))

if dados['ctps'] != 0:
    dados['contratado'] = int(input('Digite o ano contratação: '))
    idadeContrato = dados['contratado'] - anoNasc # idade que a pessoa tinha quando foi contratada
    dados['salario'] = float(input('Digite o salário: R$ '))
    dados['aposentadoria'] = idadeContrato + 35

for k, v in dados.items():
    print(f'{k} -> {v}')