palavras = ('Quetzal', 'Superstarrio', 'Run', 'Nobody')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ') 