n = int(input('Digite um número: '))
primo = True

for i in range(2, n):
    if n % i == 0:
        primo = False  # se ocorrer alguma divisão exata, saberemos que o número não é primo

if primo:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')