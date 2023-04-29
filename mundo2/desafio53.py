
frase = input('Digite uma frase para sabermos se ela é um palíndromo: ')
fraseSemEspacos = frase.replace(' ', '').upper()

if fraseSemEspacos == fraseSemEspacos[::-1]:
    print('A frase é um palíndromo!')
else:
    print('Não é um palíndromo!')


