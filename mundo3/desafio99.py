def maior(*n):
    maior = 0
    for i, x in enumerate(n):
        if i == 0:
            maior = x
        else:
            if x > maior:
                maior = x
                
    for x in n:
        print(x, end=' ')

    print(f'=> Foram passados {len(n)} valores')
    print(f'O maior valor foi {maior}')
        
maior()