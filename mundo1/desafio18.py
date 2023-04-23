from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))

print(f'O seno de {int(ang)}° é: {sin(radians(ang)):.2f}')
print(f'O cosseno de {int(ang)}° é: {cos(radians(ang)):.2f}')
print(f'A tangente de {int(ang)}° é: {tan(radians(ang)):.2f}')