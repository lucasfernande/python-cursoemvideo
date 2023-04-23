from random import shuffle

a1 = input('1° Aluno: ')
a2 = input('2° Aluno: ')
a3 = input('3° Aluno: ')
a4 = input('4° Aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)

print('A ordem de apresentação será: ')
for i in range(len(alunos)):
    print(f'{i + 1}°: {alunos[i]}')
