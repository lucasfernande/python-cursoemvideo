frase = str(input('Digite uma frase qualquer: ')).strip()

print(f'A letra A aparece {frase.upper().count("A")} vezes na frase')
print(f'A primeira letra A está na posição {frase.upper().index("A")}')
print(f'A última letra A está na posição {frase.upper().rindex("A")}')
