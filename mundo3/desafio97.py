def escreva(msg):
    t = len(msg) + 4
    print('-' * t)
    print(msg.center(t))
    print('-' * t)

escreva('Python')
escreva('Título do Programa')