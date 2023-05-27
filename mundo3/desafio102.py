def fatorial(n=1, show=False):
    """
    Função para calcular fatorial

    Args:
        n (int, optional): número a ser calculado. Padrão -> 1.
        show (bool, optional): mostrar a multiplicação. Padrão -> False.

    Returns:
        int: fatorial do número
    """
    f = 1

    for i in range(n, 0, -1):
        if show:
            print(f'{i}', 'x ' if i > 1 else '= ', end='')
        f *= i

    return f


n = int(input('Digite um número para calcular o fatorial: '))
show = str(input('Deseja mostrar a multiplicação? [S/N]: '))

show = True if show in 'Ss' else False

print(fatorial(n, show))