import files
import ler
import view

files.criar('registros.txt')

while True:
    view.menu()
    
    while True:
        opc = ler.leiaInt('\033[0;32mSua opção:\033[0m ')

        if ler.validarOpc(opc):
            break
        else:
            print('\033[0;31mErro: opção inválida\033[0m')

    if opc == 1:
        view.registros()
    
    if opc == 2:
        nome = str(input('Nome: ').strip())
        idade = ler.leiaInt('Idade: ')

        files.cadastrar(nome, idade)

    if opc == 3:
        print('Programa encerrado')
        break