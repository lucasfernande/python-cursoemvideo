from random import randint

ns = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))

print('Os números gerados foram: ', end='')
for  n in ns:
    print(n, end=' ')

print(f'\nO maior valor gerado foi: {max(ns)}')
print(f'O menor valor gerado foi: {min(ns)}')