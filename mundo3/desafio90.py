aluno = dict()

aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input('Digite a média: '))

if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'  
else: 
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k.capitalize()}: {v}')