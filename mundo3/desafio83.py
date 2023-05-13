# exp = str(input('Digite a expressão: '))

# if exp.count('(') == exp.count(')'):
#     print('Sua expressão está correta!')
# else:
#     print('Sua expressão está errada!')

exp = str(input('Digite a expressão: '))
pilha = list()

for simbolo in exp:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() # vai remover a abertura correspondente a ele
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')