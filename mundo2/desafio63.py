t1 = 0
t2 = 1
t3 = 0

cont = 1
n = int(input('Quantos termos da sequência de Fibonacci?: '))

while cont <= n:
    print(t3, end=' => ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1

print('Fim')