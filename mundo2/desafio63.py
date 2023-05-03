t1 = 0
t2 = 1
t3 = 0

n = int(input('Quantos termos da sequência de Fibonacci?: '))
cont = 3

print(f'{t1} => {t2} =>', end=' ')
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' => ')
    t1 = t2
    t2 = t3
    cont += 1

print('Fim')