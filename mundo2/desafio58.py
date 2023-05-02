from random import randint

num = randint(0, 10)
tent = 1

palpite = int(input('Digite um número de 0 a 10: '))

while palpite != num:
    if palpite > num:
        palpite = int(input('Seu palpite foi MAIOR que o número sorteado, tente outro: '))
        tent += 1
    if palpite < num:
        palpite = int(input('Seu palpite foi MENOR que o número sorteado, tente outro: '))
        tent += 1
    
print(f'Você acertou em {tent} tentativas! O número sorteado foi {num}.')