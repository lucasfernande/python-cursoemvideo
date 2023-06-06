def leiaInt(msg):
    while True:
        n = input(msg).strip()

        try:
            n = int(n)
            break
        except:
            print('\033[0;31mErro: digite um número\033[0m')
        
    return n

def validarOpc(n):
    if n not in range(1, 4):
        return False
    
    return True

    