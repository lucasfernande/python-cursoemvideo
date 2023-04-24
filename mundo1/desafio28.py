from random import randint

n = randint(0, 5)
p = int(input('Digite seu palpite de 0 a 5: '))

while p != n:
    p = int(input('Errado! Tente outro: '))

print(f'Você acertou! O número era: {n}')