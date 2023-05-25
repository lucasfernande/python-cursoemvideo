from time import sleep

def pulaLinha():
    print()
    print('-' * 30)
    
def contador(i, f, p):
    print(f'Contando de {i} até {f} de {p} em {p}')
    
    if p == 0:
        p = 1

    if p < 0:
        p *= -1

    if f > i:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(0.5)
        pulaLinha()
    else:
        while i >= f:
            print(i, end=' ')
            i -= p
            sleep(0.5)
        pulaLinha()

contador(1, 10, 1)
contador(10, 0, -2)

print('Agora faça uma contagem personalizada')
i = int(input(f'{"Início: ":<8}'))
f = int(input(f'{"Fim: ":<8}'))
p = int(input(f'{"Passo: ":<8}'))
contador(i, f, p)