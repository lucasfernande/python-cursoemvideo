nome = str(input('Digite seu nome completo: '))
print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras')
print(f'O primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')
