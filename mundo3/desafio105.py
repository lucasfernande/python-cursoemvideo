def notas(*n, sit=False):
    """
    Função para analisar notas de um aluno

    Args:
        n (tuple): notas dos alunos
        sit (bool, optional): mostrar a situação do aluno. Defaults to False.

    Returns:
        dict: análise das notas
    """
    aluno = dict()

    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n) / len(n)

    if sit:
        aluno['situacao'] = 'Aprovado' if aluno['media'] >= 6 else 'Reprovado'
    print(type(n))
    return aluno

aluno = notas(4.5, 9.5, 5, 4.5, sit=True)
print(aluno)

# help(notas)